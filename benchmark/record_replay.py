"""Record a finished run, replayed in the viewer: python -m benchmark.record_replay <run_id> [--speed 20]

Serves the repository on a local port, opens viewer/index.html in replay mode in headless Chrome at 1920x1080, records
until the replay ends, and writes agents/level_N/media/<run_id>.mp4 and a poster .jpg (a frame near the end).
"""
from __future__ import annotations

import argparse
import functools
import http.server
import shutil
import subprocess
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
from . import paths
PORT = 8791


def serve() -> http.server.ThreadingHTTPServer:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    handler.log_message = lambda *a, **k: None
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def record(run_id: str, speed: float, cap: float, hold: float) -> Path:
    OUT = paths.level_dir(paths.parse(run_id)["level"]) / "media"
    OUT.mkdir(parents=True, exist_ok=True)
    raw = OUT / "raw" / run_id
    shutil.rmtree(raw, ignore_errors=True)
    raw.mkdir(parents=True)
    srv = serve()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(channel="chrome", headless=True)
            ctx = b.new_context(viewport={"width": 1920, "height": 1080}, record_video_dir=str(raw),
                                record_video_size={"width": 1920, "height": 1080})
            pg = ctx.new_page()
            pg.goto(f"http://127.0.0.1:{PORT}/viewer/index.html?run={run_id}&replay=1&speed={speed}&cap={cap}&hold={hold}")
            pg.wait_for_function("document.body.dataset.replayDone === '1'", timeout=60 * 60 * 1000)
            ctx.close()
            b.close()
    finally:
        srv.shutdown()
    webm = next(raw.glob("*.webm"))
    mp4 = OUT / f"{run_id}.mp4"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(webm), "-vf", "fps=30,format=yuv420p",
                    "-c:v", "libx264", "-crf", "22", "-preset", "medium", "-an", "-movflags", "+faststart", str(mp4)], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
                               capture_output=True, text=True).stdout.strip() or 0)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", str(max(0.0, dur - 3)), "-i", str(mp4),
                    "-frames:v", "1", "-q:v", "3", str(mp4.with_suffix(".jpg"))], check=True)
    print(f"{mp4} {dur:.1f} s")
    return mp4


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("run_id")
    ap.add_argument("--speed", type=float, default=20)
    ap.add_argument("--cap", type=float, default=0.8)
    ap.add_argument("--hold", type=float, default=6)
    a = ap.parse_args()
    record(a.run_id, a.speed, a.cap, a.hold)
