# Verificador da triagem por resumo
Você é um verificador independente. Você recebe os resumos dos candidatos, baixados por código das bases
acadêmicas, e a decisão de triagem. Para CADA artigo incluído, confira no resumo fornecido se ele atende a cada
critério do pedido (tema, estudo empírico, recorte). Reprove a triagem se algum incluído não atende, e diga qual e
por quê. Período, tipo de publicação e DOI já foram conferidos por código no Crossref; não reprove por eles. Se menos
artigos que o pedido atendem a todos os critérios, entregar menos é o CORRETO: não reprove por quantidade e nunca
peça para incluir artigo que não atende só para completar o número. Use só os resumos fornecidos.

COMO RESPONDER
- approved: false só por ERRO REAL que compromete o resultado (dado errado, critério do pedido violado ou
  esquecido, fonte que não existe, citação que não está na fonte, afirmação que a fonte não sustenta).
  Sugestão de melhoria, preferência de estilo ou cobertura que poderia ser maior não reprova: aprove e ponha a
  sugestão em feedback.
- checked: o que você conferiu, um item por linha, concreto (por exemplo: 'DOI 10.x abre e o título confere').
- issues: cada problema numa frase curta que um estudante entenda: o que está errado ou faltou, e onde.
- feedback: o que o executor precisa fazer na próxima tentativa.
- Escreva em português do Brasil, sem travessão.

PEDIDO DO PESQUISADOR:
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2019 e 2025, sobre como as pessoas percebem, detectam ou avaliam a credibilidade de imagens, vídeos e áudios sintéticos gerados por inteligência artificial (deepfakes, rostos sintéticos e clones de voz). Restrições: apenas estudos empíricos com participantes humanos (experimentos, testes de detecção, surveys ou medidas fisiológicas); exclua artigos sobre algoritmos de detecção automática, estudos centrados em políticos, eleições ou propaganda política e estudos sobre saúde. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CRITÉRIOS:
{
 "include": [
  "Artigo de periódico revisado por pares, publicado entre 2019 e 2025",
  "Estudo empírico com dados próprios coletados de participantes humanos (experimento, teste de detecção, survey ou medidas fisiológicas como eye tracking, EEG, condutância da pele)",
  "Foco em como pessoas percebem, detectam ou avaliam a credibilidade, autenticidade ou confiabilidade de mídia sintética gerada por IA: deepfakes em vídeo, imagens/rostos sintéticos ou áudio/clones de voz",
  "Resumo que permita identificar método e, de preferência, o tamanho da amostra"
 ],
 "exclude": [
  "Artigos sobre algoritmos ou modelos de detecção automática de deepfakes (aprendizado de máquina, redes neurais) sem foco em participantes humanos",
  "Estudos centrados em políticos, eleições, campanhas ou propaganda política",
  "Estudos sobre saúde (desinformação em saúde, COVID-19, vacinas, aplicações clínicas)",
  "Revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos ou conceituais, resenhas",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, teses e dissertações",
  "Artigos sem dados empíricos próprios ou sem participantes humanos (por exemplo, apenas análise de conteúdo, propostas de datasets ou estudos técnicos)",
  "Publicações fora do período 2019 a 2025"
 ]
}

ARTIGOS INCLUÍDOS, COM O RESUMO BAIXADO POR CÓDIGO:
[
 {
  "id": "C94",
  "title": "Fooled twice: People cannot detect deepfakes but think they can",
  "year": 2021,
  "venue": "iScience",
  "abstract": "Hyper-realistic manipulation of audio-visual content, i.e., deepfakes, presents a new challenge for establishing veracity of online content. Research on the human impact of deepfakes, addressing both behaviors in response to and cognitive processing of deepfakes, remains sparse. In a pre-registered behavioral experiment ( N = 210), we show that (a) people cannot reliably detect deepfakes, and (b) neither raising awareness nor introducing financial incentives improves their detection accuracy. Zeroing in on the underlying cognitive processes, we find that (c) people are biased towards mistaking deepfakes as authentic videos (rather than vice versa) and (d) overestimate their own detection abilities. Together, these results suggest that people adopt a ``seeing-is-believing'' heuristic for deepfake detection while being overconfident in their (low) detection abilities. The combination renders people particularly susceptible to be influenced by inauthentic deepfake content.",
  "reason": "Experimento pré-registrado (N=210) mostrando que pessoas não detectam deepfakes e superestimam sua habilidade."
 },
 {
  "id": "C71",
  "title": "Deepfake detection by human crowds, machines, and machine-informed crowds",
  "year": 2021,
  "venue": "Proceedings of the National Academy of Sciences",
  "abstract": "The recent emergence of machine-manipulated media raises an important societal question: How can we know whether a video that we watch is real or fake? In two online studies with 15,016 participants, we present authentic videos and deepfakes and ask participants to identify which is which. We compare the performance of ordinary human observers with the leading computer vision deepfake detection model and find them similarly accurate, while making different kinds of mistakes. Together, participants with access to the model's prediction are more accurate than either alone, but inaccurate model predictions often decrease participants' accuracy. To probe the relative strengths and weaknesses of humans and machines as detectors of deepfakes, we examine human and machine performance across video-level features, and we evaluate the impact of preregistered randomized interventions on deepfake detection. We find that manipulations designed to disrupt visual processing of faces hinder human participants' performance while mostly not affecting the model's performance, suggesting a role for specialized cognitive capacities in explaining human deepfake detection performance.",
  "reason": "Dois estudos online com 15.016 participantes sobre detecção humana de deepfakes versus modelo."
 },
 {
  "id": "C25",
  "title": "Testing human ability to detect ‘deepfake’ images of human faces",
  "year": 2023,
  "venue": "Journal of Cybersecurity",
  "abstract": "Abstract ‘Deepfakes’ are computationally created entities that falsely represent reality. They can take image, video, and audio modalities, and pose a threat to many areas of systems and societies, comprising a topic of interest to various aspects of cybersecurity and cybersafety. In 2020, a workshop consulting AI experts from academia, policing, government, the private sector, and state security agencies ranked deepfakes as the most serious AI threat. These experts noted that since fake material can propagate through many uncontrolled routes, changes in citizen behaviour may be the only effective defence. This study aims to assess human ability to identify image deepfakes of human faces (these being uncurated output from the StyleGAN2 algorithm as trained on the FFHQ dataset) from a pool of non-deepfake images (these being random selection of images from the FFHQ dataset), and to assess the effectiveness of some simple interventions intended to improve detection accuracy. Using an online survey, participants (N = 280) were randomly allocated to one of four groups: a control group, and three assistance interventions. Each participant was shown a sequence of 20 images randomly selected from a pool of 50 deepfake images of human faces and 50 images of real human faces. Participants were asked whether each image was AI-generated or not, to report their confidence, and to describe the reasoning behind each response. Overall detection accuracy was only just above chance and none of the interventions significantly improved this. Of equal concern was the fact that participants’ confidence in their answers was high and unrelated to accuracy. Assessing the results on a per-image basis reveals that participants consistently found certain images easy to label correctly and certain images difficult, but reported similarly high confidence regardless of the image. Thus, although participant accuracy was 62% overall, this accuracy across images ranged quite evenly between 85 and 30%, with an accuracy of below 50% for one in every five images. We interpret the findings as suggesting that there is a need for an urgent call to action to address this threat.",
  "reason": "Survey online experimental (N=280) sobre detecção humana de rostos StyleGAN2."
 },
 {
  "id": "C55",
  "title": "AI Hyperrealism: Why AI Faces Are Perceived as More Real Than Human Ones",
  "year": 2023,
  "venue": "Psychological Science",
  "abstract": "Recent evidence shows that AI-generated faces are now indistinguishable from human faces. However, algorithms are trained disproportionately on White faces, and thus White AI faces may appear especially realistic. In Experiment 1 ( N = 124 adults), alongside our reanalysis of previously published data, we showed that White AI faces are judged as human more often than actual human faces—a phenomenon we term AI hyperrealism. Paradoxically, people who made the most errors in this task were the most confident (a Dunning-Kruger effect). In Experiment 2 ( N = 610 adults), we used face-space theory and participant qualitative reports to identify key facial attributes that distinguish AI from human faces but were misinterpreted by participants, leading to AI hyperrealism. However, the attributes permitted high accuracy using machine learning. These findings illustrate how psychological theory can inform understanding of AI outputs and provide direction for debiasing AI algorithms, thereby promoting the ethical use of AI.",
  "reason": "Dois experimentos (N=124 e N=610) mostrando rostos de IA julgados mais humanos que reais."
 },
 {
  "id": "C57",
  "title": "Warning: Humans cannot reliably detect speech deepfakes",
  "year": 2023,
  "venue": "PLoS ONE",
  "abstract": "Speech deepfakes are artificial voices generated by machine learning models. Previous literature has highlighted deepfakes as one of the biggest security threats arising from progress in artificial intelligence due to their potential for misuse. However, studies investigating human detection capabilities are limited. We presented genuine and deepfake audio to n = 529 individuals and asked them to identify the deepfakes. We ran our experiments in English and Mandarin to understand if language affects detection performance and decision-making rationale. We found that detection capability is unreliable. Listeners only correctly spotted the deepfakes 73% of the time, and there was no difference in detectability between the two languages. Increasing listener awareness by providing examples of speech deepfakes only improves results slightly. As speech synthesis algorithms improve and become more realistic, we can expect the detection task to become harder. The difficulty of detecting speech deepfakes confirms their potential for misuse and signals that defenses against this threat are needed.",
  "reason": "Experimento com n=529 sobre detecção humana de deepfakes de fala."
 },
 {
  "id": "C07",
  "title": "AI-generated images of familiar faces are indistinguishable from real photographs",
  "year": 2025,
  "venue": "Cognitive Research Principles and Implications",
  "abstract": "Abstract Human users are now able to generate synthetic face images with artificial intelligence (AI) tools. Although indistinguishable from real photographs, these images have tended to feature fictional identities that do not exist in the real world. As a result, their use in applied contexts, including the spread of fake information, is similarly limited. Here, we investigated a new method for generating face images (via ChatGPT plus DALL·E) and its application to both fictional and real (in this case, celebrity) identities. Our results demonstrated that generated images of both fictional (Experiment 1) and celebrity identities (Experiment 2) could not be distinguished from real photographs. Further, providing additional real photographs for comparison during the task resulted in limited gains (Experiments 3 and 4). Finally, prior familiarity with celebrity faces produced only modest performance improvements. Therefore, new methods of detection should be explored as a matter of urgency since the latest ‘off the shelf’ AI tools can now generate face images of real people that are essentially undetectable as synthetic to most human observers.",
  "reason": "Experimentos de detecção humana de rostos gerados por IA (ChatGPT/DALL·E), fictícios e de celebridades."
 },
 {
  "id": "C02",
  "title": "Training human super-recognizers’ detection and discrimination of AI-generated faces",
  "year": 2025,
  "venue": "Royal Society Open Science",
  "abstract": "Generative adversarial networks (GANs) can create realistic synthetic faces, which have the potential to be used for nefarious purposes. The synthetic faces produced by GANs are difficult to detect and are often judged to be more realistic than real faces. Training programmes have been developed to improve human synthetic face detection accuracy, with mixed results. Here, we investigate synthetic face detection and discrimination in super-recognizers (SRs; who have exceptional face recognition skills), and typical-ability control participants. We also devised a training procedure which sought to highlight rendering artefacts. In two different experimental designs, we found that SRs (total N = 283) were better at detecting and discriminating synthetic faces than controls (total N = 381), where control participants were below chance without training. Trained SRs and controls had significantly better performance than those without training, and the magnitude of the training effect was similar in both groups. Our results suggest that SRs are using cues unrelated to rendering artefacts to detect and discriminate synthetic faces, and that an easily implementable training procedure increases their performance to above chance levels. These results have implications for real-world scenarios, where trained SRs' performance could be harnessed for synthetic face detection.",
  "reason": "Experimentos com humanos (super-recognizers e controles, N=283 e N=381) sobre detecção de rostos sintéticos."
 },
 {
  "id": "C08",
  "title": "Crowds Improve Human Detection of AI ‐Synthesised Faces",
  "year": 2024,
  "venue": "Applied Cognitive Psychology",
  "abstract": "ABSTRACT Artificial intelligence can now synthesise face images which people cannot distinguish from real faces. Here, we investigated the wisdom of the (outer) crowd (averaging individuals' responses to the same trial) and inner crowd (averaging the same individual's responses to the same trial after completing the test twice) as routes to increased performance. In Experiment 1, participants viewed synthetic and real faces, and rated whether they thought each face was synthetic or real using a 1–7 scale. Each participant completed the task twice. Inner crowds showed little benefit over individual responses, and we found no associations between performance and personality factors. However, we found increases in performance with increasing sizes of outer crowd. In Experiment 2, participants judged each face only once, providing a binary ‘synthetic/real’ response, along with a confidence rating and an estimate of the percentage of other participants that they thought agreed with their answer. We compared three methods of aggregation for outer crowd decisions, finding that the majority vote provided the best performance for small crowds. However, the ‘surprisingly popular’ solution outperformed the majority vote and the confidence‐weighted approach for larger crowds. Taken together, we demonstrate the use of outer crowds as a robust method of improvement during synthetic face detection, comparable with previous approaches based on training interventions.",
  "reason": "Dois experimentos com participantes julgando rostos sintéticos vs. reais (desempenho individual e de multidões)."
 },
 {
  "id": "C43",
  "title": "A (Mid)journey Through Reality: Assessing Accuracy, Impostor Bias, and Automation Bias in Human Detection of AI‐Generated Images",
  "year": 2025,
  "venue": "Human Behavior and Emerging Technologies",
  "abstract": "While the challenge of distinguishing AI‐generated from real images is widely acknowledged, the specific cognitive biases that systematically shape human judgment in this domain remain poorly understood. It is particularly unclear how a general awareness of AI capabilities fosters novel biases, like a pervasive skepticism (“impostor bias”), and how this interacts with established phenomena like “automation bias”. This study addresses this gap by providing the first quantitative analysis of how these two biases operate across five distinct experimental variants designed to test the context‐dependency of human perception. Through a mixed‐methods study with 746 participants, we demonstrate that human authentication accuracy hovered around chance levels (ranging from 47.0% to 55.5%). However, our analysis provides robust evidence for the systematic operation of cognitive biases. We validate the presence of “impostor bias” through a consistent pattern of higher doubt for AI‐generated images and confirm “automation bias” through significant opinion changes following algorithmic suggestions. Our findings reveal that these biases are not uniform across populations: gender was a consistent predictor of automation bias, with males in all five variants showing a significantly stronger and more consistent tendency (Cohen’s d = 0.254–0.683) to be influenced by algorithmic suggestions. In contrast, age and academic background had minimal and highly localized effects. Furthermore, we identified a significant interaction between experimental stimuli and performance over time, isolating a pronounced fatigue effect to a single questionnaire variant where accuracy progressively declined (by approximately 1.7% per trial). By integrating human feedback with Grad‐CAM visualizations, we confirm a divergence between human holistic evaluation and the localized focus of machine learning models. These findings carry direct implications for policy, as discussed within the context of the European AI Act, and inform the design of human–AI systems and media literacy programs aimed at mitigating these critical cognitive vulnerabilities.",
  "reason": "Estudo com 746 participantes sobre detecção humana de imagens de IA e vieses (impostor, automação)."
 },
 {
  "id": "C58",
  "title": "Deciphering authenticity in the age of AI: how AI-generated disinformation images and AI detection tools influence judgements of authenticity",
  "year": 2025,
  "venue": "AI &amp; SOCIETY",
  "abstract": "Abstract An ongoing surge of Artificial Intelligence (AI)-enabled false content has been spreading its way through the information ecosystem, including AI-generated images, which have been used as part of political disinformation campaigns. Thus, there remains a pressing need to understand which factors individuals rely upon when determining whether images are AI-generated, particularly when they can be used to spread disinformation. AI-generated images have been characterised by their aesthetic realism, which can be leveraged to deceive users, and those who use generative AI to create deceptive content also tend to exploit its ability to convey and elicit emotion. This experimental study explored how aesthetic realism and emotional salience, as key features of both AI-generated content and disinformation, may influence authenticity judgements of AI-generated disinformation images. In this study, 292 UK-based participants were presented with both AI-generated and non-AI-generated disinformation images which varied in aesthetic realism and emotional salience. Results showed that participants were more likely to judge realistic-looking AI-generated images as being authentic compared with less realistic-looking AI-generated images, but did so with less confidence in their decision. Emotional salience was not a significant predictor of judgements. When participants were presented with the correct verdict of an AI detection tool, their reliance on the tool to update their own judgements was predicted by the aesthetic realism of the image and their confidence levels. These findings may assist with the development of disinformation detection tools, as well as strategies that mitigate the spread of deceptive, synthesised visual content in the digital age.",
  "reason": "Experimento com 292 participantes sobre julgamento de autenticidade de imagens geradas por IA e uso de ferramenta de detecção."
 },
 {
  "id": "C44",
  "title": "Deepfake smiles matter less—the psychological and neural impact of presumed AI-generated faces",
  "year": 2023,
  "venue": "Scientific Reports",
  "abstract": "Abstract High-quality AI-generated portraits (“deepfakes”) are becoming increasingly prevalent. Understanding the responses they evoke in perceivers is crucial in assessing their societal implications. Here we investigate the impact of the belief that depicted persons are real or deepfakes on psychological and neural measures of human face perception. Using EEG, we tracked participants’ (N = 30) brain responses to real faces showing positive, neutral, and negative expressions, after being informed that they are either real or fake. Smiling faces marked as fake appeared less positive, as reflected in expression ratings, and induced slower evaluations. Whereas presumed real smiles elicited canonical emotion effects with differences relative to neutral faces in the P1 and N170 components (markers of early visual perception) and in the EPN component (indicative of reflexive emotional processing), presumed deepfake smiles showed none of these effects. Additionally, only smiles presumed as fake showed enhanced LPP activity compared to neutral faces, suggesting more effortful evaluation. Negative expressions induced typical emotion effects, whether considered real or fake. Our findings demonstrate a dampening effect on perceptual, emotional, and evaluative processing of presumed deepfake smiles, but not angry expressions, adding new specificity to the debate on the societal impact of AI-generated content.",
  "reason": "Estudo com EEG (N=30) sobre avaliação de rostos presumidos como deepfake."
 },
 {
  "id": "C97",
  "title": "Uncovering strategies for identifying deepfakes",
  "year": 2025,
  "venue": "Information Research",
  "abstract": "Introduction. The proliferation of generative artificial intelligence tools capable of producing high-quality videos that can masquerade as genuine content has raised concerns about online misinformation. This study investigates human ability to identify deepfake videos, with a focus on identification performance and the strategies employed. Method. Data was collected through an online survey. Participants were young adults aged 21 to 35. They were shown four videos and asked to identify them as real or deepfake, followed by questions about the identification strategies used. Results. Our results revealed the diverse range of strategies utilised. Predominant strategies centre around assessing the authenticity of traits pertaining to the video's subject as opposed to peripheral details. Furthermore, we uncovered preferences for intuition and strategies that relate to individual decision-making over consulting other individuals or online materials. Conclusion. Our results help enhance understanding of how people identify deepfake videos, adding to existing knowledge. These findings also inform initiatives aimed at educating the public about spotting deepfakes.",
  "reason": "Survey online sobre desempenho e estratégias humanas para identificar vídeos deepfake."
 },
 {
  "id": "C24",
  "title": "Partial Fake Speech Attacks in the Real World Using Deepfake Audio",
  "year": 2025,
  "venue": "Journal of Cybersecurity and Privacy",
  "abstract": "Advances in deep learning have led to dramatic improvements in generative synthetic speech, eliminating robotic speech patterns to create speech that is indistinguishable from a human voice. Although these advances are extremely useful in various applications, they also facilitate powerful attacks against both humans and machines. Recently, a new type of speech attack called partial fake (PF) speech has emerged. This paper studies how well humans and machines, including speaker recognition systems and existing fake-speech detection tools, can distinguish between human voice and computer-generated speech. Our study shows that both humans and machines can be easily deceived by PF speech, and the current defences against PF speech are insufficient. These findings emphasise the urgency of increasing awareness for humans and creating new automated defences against PF speech for machines.",
  "reason": "Estuda como humanos e máquinas distinguem fala parcialmente falsa de voz humana; humanos são enganados."
 },
 {
  "id": "C28",
  "title": "Perception and deception: Exploring individual responses to deepfakes across different modalities",
  "year": 2023,
  "venue": "Heliyon",
  "abstract": "This study is one of the first to investigate the relationship between modalities and individuals' tendencies to believe and share different forms of deepfakes (also deep fakes). Using an online survey experiment conducted in the US, participants were randomly assigned to one of three disinformation conditions: video deepfakes, audio deepfakes, and cheap fakes to test the effect of single modality against multimodality and how it affects individuals' perceived claim accuracy and sharing intentions. In addition, the impact of cognitive ability on perceived claim accuracy and sharing intentions between conditions are also examined. The results suggest that individuals are likelier to perceive video deepfakes as more accurate than cheap fakes, but not audio deepfakes. Yet, individuals are more likely to share video deepfakes than cheap and audio deepfakes. We also found that individuals with high cognitive ability are less likely to perceive deepfakes as accurate or share them across formats. The findings emphasize that deepfakes are not monolithic, and associated modalities should be considered when studying user engagement with deepfakes.",
  "reason": "Experimento de survey sobre precisão percebida e compartilhamento de deepfakes de vídeo, áudio e cheap fakes."
 },
 {
  "id": "C12",
  "title": "The Relationship of Digital Literacy, Exposure to AI-Generated Deepfake Videos, and the Ability to Identify Deepfakes in Generation X Hubungan Literasi Digital, Paparan Video Deepfake yang Dihasilkan AI, dan Kemampuan untuk Mengidentifikasi Deepfake pada Generasi X",
  "year": 2024,
  "venue": "Jurnal Pekommas",
  "abstract": "The study explores the relationship between digital literacy, exposure to AI-generated deepfake videos, and the ability to identify deepfakes by Generation X in Indonesia who are currently between the ages of 43 and 58. It also analyzes the impact of deepfake identification capabilities on the cognitive, affective, and behavioral aspects of internet users. Through a survey involving 199 respondents taken from a total population of 42 million Generation X internet users in Indonesia, it applied a random sampling method. The sample size was determined by the Slovin formula with a confidence level of 90% and a margin of error of 7.1%. The descriptive analysis shows a moderate level of digital literacy and relatively low exposure to deepfakes. However, the ability to identify deepfakes was found to be low. The results of inferential statistical analysis show that digital literacy and exposure to deepfakes do not have a significant influence on the ability to identify deepfakes. Additionally, the ability to identify deepfakes does not significantly affect cognition, compassion, or behavior. While digital literacy is important, these findings reinforce the assumptions of Generation Theory and Media Dependency Theory. Additionally, it suggests that specific training on media manipulation technologies is needed to improve deepfake detection capabilities. This research implies that efforts to improve digital literacy should be expanded, including technical skills and critical thinking relevant to manipulative media such as deepfakes.",
  "reason": "Survey com 199 respondentes sobre capacidade de identificar vídeos deepfake."
 },
 {
  "id": "C41",
  "title": "“There Is something Rotten in Denmark”: Investigating the Deepfake persona perceptions and their Implications for human-centered AI",
  "year": 2023,
  "venue": "Computers in Human Behavior Artificial Humans",
  "abstract": "Although they often have a negative connotation due to their social risks, deepfakes have the potential to improve HCI, human-centered AI, and user experience (UX). To investigate the impact of deepfakes on persona UX, we conducted an experimental study with 46 users who used a deepfake persona and a human persona to carry out a design task. We collected think-aloud, observant notes, and survey data. The results of our mixed-method analysis indicate that if users observe glitches in the deepfake personas, these glitches have a detrimental effect on the persona UX and task performance; however, not all users identify glitches. Our quantitative analysis of survey data shows that there are differences in how (a) users perceive deepfakes, (b) users detect deepfake glitches, (c) deepfake glitches affect information comprehension, and (d) deepfake glitches affect task completion. Glitches have the most significant impact on authenticity, persona perception, and task perception variables but less impact on behavioral variables. The results imply that organizations implementing deepfake personas need to address perceptual challenges before the full potential of deepfake technology can be realized for persona creation.",
  "reason": "Experimento com 46 usuários sobre percepção de autenticidade e detecção de falhas em persona deepfake."
 },
 {
  "id": "C111",
  "title": "The realness of fakes: Primary evidence of the effect of deepfake personas on user perceptions in a design task",
  "year": 2023,
  "venue": "International Journal of Human-Computer Studies",
  "abstract": "Deepfakes, realistic portrayals of people that do not exist, have garnered interest in research and industry. Yet, the contributions of deepfake technology to human-computer interaction remain unclear. One possible value of deepfake technology is to create more immersive user personas. To test this premise, we use a commercial-grade service to generate three deepfake personas (DFs). We also create counterparts of the same persona in two traditional modalities: classic and narrative personas. We then investigate how persona modality affects the perceptions and task performance of the persona user. Our findings show that the DFs were perceived as less empathetic, credible, complete, clear, and immersive than other modalities. Participants also indicated less willingness to use the DFs and less sense of control, but there were no differences in task performance. We also found a strong correlation between the uncanny valley effect and other user perceptions, implying that the tested deepfake technology might lack maturity for personas, negatively affecting user experience. Designers might also be accustomed to using traditional persona profiles. Further research is needed to investigate the potential and downsides of DFs.",
  "reason": "Experimento sobre percepção de credibilidade e outras avaliações de personas deepfake."
 },
 {
  "id": "C119",
  "title": "Examining the role of compression in influencing AI-generated image authenticity",
  "year": 2025,
  "venue": "Scientific Reports",
  "abstract": "The rapid development of AI-generated Content (AIGC) in recent years has narrowed the gap between virtual and realistic. Among them, AI-generated Images (AIGIs) are particularly significant, as their emergence has led to a profound impact on education, art, virtual reality, etc. However, little research has been conducted to investigate whether compression artifacts can influence the subjective authenticity of AIGIs. In this paper, we systematically study this problem by creating the first-ever AIGC image dataset for subjective evaluations of authenticity discrimination. The dataset contains 500 AIGIs and 500 natural images with a resolution of 768 × 768. The content of the images therein has been categorized into 5 major categories and 20 subcategories to study the performance of AIGIs on different contents. Subsequently, we introduce four varying degrees of compression distortion (QP = 22, 32, 42, 52) on all images utilizing the standard Versatile Video Coding (VVC). It is interesting to find that with an increase in compression distortion, the accuracy of human vision in determining the AIGIs descends. The proposed study is expected to shed light on future research that aims to achieve a good balance between authenticity and visual quality.",
  "reason": "Avaliação subjetiva humana da autenticidade de imagens de IA sob compressão; acurácia humana cai com compressão (amostra não informada)."
 },
 {
  "id": "C64",
  "title": "DEEPFAKES E PROVA DIGITAL NA VIOLÊNCIA DOMÉSTICA: OS RISCOS DA INTELIGÊNCIA ARTIFICIAL DEEPFAKES AND DIGITAL EVIDENCE IN DOMESTIC VIOLENCE: THE RISKS OF ARTIFICIAL INTELLIGENCE DEEPFAKES Y PRUEBA DIGITAL EN LA VIOLENCIA DOMÉSTICA: LOS RIESGOS DE LA INTELIGENCIA ARTIFICIAL",
  "year": 2025,
  "venue": "Novos Estudos Jurí­dicos",
  "abstract": "Contextualização: Os avanços recentes da inteligência artificial generativa têm introduzido novos desafios ao sistema de justiça penal, em particular no domínio da prova digital. Entre as aplicações mais problemáticas destacam-se os deepfakes, suscetíveis de induzir em erro quanto à sua autenticidade, especialmente em contextos de maior fragilidade probatória, como os crimes de violência doméstica. Objetivos: O presente estudo tem como objetivo geral compreender as perceções, experiências e práticas dos/as magistrados/as relativamente à admissibilidade e valoração da prova digital, com especial enfoque nos meios de prova audiovisual e nos riscos associados à sua eventual manipulação por tecnologias de inteligência artificial generativa. Método: Foi adotada uma abordagem qualitativa, recorrendo-se à realização de entrevistas semiestruturadas a oito magistrados/as, com experiência profissional em processos de violência doméstica. Resultados: Observaram-se limitações na deteção de elementos audiovisuais gerados ou manipulados por inteligência artificial. A autenticidade deste tipo de elementos (deepfakes) granjearam mais credibilidade que elementos autênticos. De todo o modo, embora a prova audiovisual seja considerada relevante, o depoimento da vítima continua sendo considerado a “prova rainha”.",
  "reason": "Entrevistas com 8 magistrados sobre capacidade de detectar e credibilidade de deepfakes como prova; dados próprios, qualitativo (método menos central)."
 },
 {
  "id": "C123",
  "title": "Pengaruh Teknologi Deepfake terhadap Kredibilitas Berita dan Jurnalistik",
  "year": 2025,
  "venue": "Komunika Jurnal Ilmiah Komunikasi",
  "abstract": "This raises concerns about the credibility of news and journalism, as deepfakes can be used to spread false information and manipulate public opinion. The purpose of this study is to discuss the impact of deepfake technology on news credibility, to compare it with previous research, and to evaluate the relevance of the findings to the current journalistic context. This study has important implications for journalism practitioners in facing new challenges from this technological advancement. The purpose of this study is to analyze the impact of deepfake technology on news and journalism credibility. Data collection methods used in this study include surveys, interviews, field experiments, and participant observation. Data analysis was carried out using descriptive statistical techniques and inferential analysis. Data from the survey and field experiments will be processed and analyzed to determine the level of change in perceptions of news credibility along with the use of deepfake technology. The results of the study indicate that deepfake technology has a significant impact on news and journalism credibility. According to the data collected, the use of deepfake in news production has led to a decline in public trust in the information presented by the media. In addition, these findings also highlight the importance of regulation and control in the application of deepfake technology in journalism to minimize the risk of spreading fake news and information manipulation. This emphasizes the need for a cautious approach to the use of technology that can damage the integrity of information and disrupt the fair and accurate reporting process. Cooperation between the media, government, and technologists is needed to overcome the negative consequences of deepfake in journalism. All parties must be responsible for ensuring the truth and fairness in presenting information to the public.",
  "reason": "Estudo com survey, entrevistas e experimentos sobre percepção de credibilidade de notícias com deepfake; resumo vago e sem amostra (baixa prioridade)."
 }
]