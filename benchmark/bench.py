"""Run a batch of runs, each in its own process:
python -m benchmark.bench --topics a01,a02,a03,a04,a05,a06 --levels n0,n1,n2,n3 --reps 2 --tag mytest --workers 4

The longest levels start first. A run that ends in error is retried once; runs that already ended as done, paused or
failed are kept. Progress goes to benchmark/progress/<tag>.jsonl.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time

from . import paths

ORDER = {"n2": 0, "n3": 1, "n1": 2, "n0": 3}


async def main_async(a) -> None:
    jobs = [(lv, t, r) for r in range(1, a.reps + 1) for lv in sorted(a.levels, key=ORDER.get) for t in a.topics]
    log = paths.ROOT / "benchmark" / "progress" / f"{a.tag}.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)

    def note(**kw):
        with log.open("a", encoding="utf-8") as f:
            f.write(json.dumps({**kw, "at": time.strftime("%Y-%m-%d %H:%M:%S")}, ensure_ascii=False) + "\n")

    note(event="start", jobs=len(jobs), levels=a.levels, topics=a.topics, reps=a.reps)
    queue: asyncio.Queue = asyncio.Queue()
    for j in jobs:
        queue.put_nowait(j)

    async def worker(w: int):
        while not queue.empty():
            lv, t, r = queue.get_nowait()
            run_id = paths.make_run_id(a.tag, lv, t, r)
            d = paths.run_dir(run_id)
            if a.skip_started and (d / "events.jsonl").exists() and not (d / "meta.json").exists():
                note(event="skip_running_elsewhere", run_id=run_id)
                continue
            for attempt in (1, 2):
                if (d / "meta.json").exists():
                    st = json.loads((d / "meta.json").read_text(encoding="utf-8"))["status"]
                    if st in ("done", "paused", "failed"):
                        break
                t0 = time.time()
                proc = await asyncio.create_subprocess_exec(
                    sys.executable, "-m", "benchmark.run", "--level", lv, "--topic", t, "--tag", a.tag,
                    "--rep", str(r), cwd=str(paths.ROOT), stdout=asyncio.subprocess.DEVNULL,
                    stderr=asyncio.subprocess.PIPE)
                _, err = await proc.communicate()
                meta = d / "meta.json"
                st = json.loads(meta.read_text(encoding="utf-8"))["status"] if meta.exists() else "error"
                note(event="run", run_id=run_id, status=st, attempt=attempt, seconds=round(time.time() - t0),
                     worker=w, error=(err.decode("utf-8", "replace")[-400:] if st == "error" else None))
                if st != "error":
                    break

    await asyncio.gather(*(worker(w) for w in range(a.workers)))
    note(event="end")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--topics", required=True, type=lambda s: s.split(","))
    ap.add_argument("--levels", default="n0,n1,n2,n3", type=lambda s: s.split(","))
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--skip-started", action="store_true", help="skip runs another dispatcher has already started")
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
