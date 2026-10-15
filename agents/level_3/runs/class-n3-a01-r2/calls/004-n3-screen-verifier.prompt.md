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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre o efeito de influência continuada da informação falsa (continued influence effect), isto é, o quanto as pessoas continuam a se apoiar em uma informação falsa depois de ela ser corrigida ou retratada. Restrições: apenas experimentos com participantes humanos que meçam crença ou raciocínio depois de uma correção ou retratação; os materiais devem ser neutros (cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde); exclua estudos com desinformação política, eleitoral, sobre vacinas ou sobre COVID-19. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CRITÉRIOS:
{
 "include": [
  "Artigo de periódico revisado por pares com estudo empírico e dados próprios",
  "Publicado entre 2018 e 2025",
  "Experimento com participantes humanos",
  "Mede crença, memória ou raciocínio inferencial após uma correção ou retratação de informação falsa",
  "Investiga o efeito de influência continuada (continued influence effect) ou persistência da dependência de informação corrigida",
  "Materiais neutros: cenários fictícios, relatos de eventos inventados ou alegações sem conotação política ou de saúde",
  "Resumo disponível que permita extrair achado principal e trecho literal"
 ],
 "exclude": [
  "Revisões de literatura, revisões sistemáticas e meta-análises",
  "Ensaios teóricos, comentários, editoriais e resenhas",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, teses e dissertações",
  "Desinformação política ou eleitoral",
  "Desinformação sobre vacinas, saúde ou COVID-19",
  "Estudos sem correção ou retratação (apenas exposição à desinformação ou detecção de notícias falsas)",
  "Estudos com modelos computacionais ou algoritmos sem participantes humanos",
  "Estudos sobre fake news em redes sociais sem medida de crença após correção",
  "Estudos fora do período 2018 a 2025",
  "Artigos sem resumo ou sem dados empíricos próprios"
 ]
}

ARTIGOS INCLUÍDOS, COM O RESUMO BAIXADO POR CÓDIGO:
[
 {
  "id": "C11",
  "title": "Can you believe it? An investigation into the impact of retraction source credibility on the continued influence effect",
  "year": 2021,
  "venue": "Memory & Cognition",
  "abstract": "The continued influence effect refers to the finding that people often continue to rely on misinformation in their reasoning even if the information has been retracted. The present study aimed to investigate the extent to which the effectiveness of a retraction is determined by its credibility. In particular, we aimed to scrutinize previous findings suggesting that perceived trustworthiness but not perceived expertise of the retraction source determines a retraction's effectiveness, and that continued influence arises only if a retraction is not believed. In two experiments, we found that source trustworthiness but not source expertise indeed influences retraction effectiveness, with retractions from low-trustworthiness sources entirely ineffective. We also found that retraction belief is indeed a predictor of continued reliance on misinformation, but that substantial continued influence effects can still occur with retractions designed to be and rated as highly credible.",
  "reason": "Dois experimentos sobre a credibilidade da fonte da retratação e a dependência da desinformação."
 },
 {
  "id": "C48",
  "title": "Relative source credibility affects the continued influence effect: Evidence of rationality in the CIE",
  "year": 2024,
  "venue": "Cognition",
  "abstract": "The Continued Influence Effect (CIE) is the phenomenon that retracted information often continues to influence judgments and inferences. The CIE is rational when the source that retracts the information (the retractor ) is less credible than the source that originally presented the information (the informant ; Connor Desai et al., 2020). Conversely, a CIE is not rational when the retractor is at least as credible as the informant. Thus, a rational account predicts that the CIE depends on the relative credibility of informant and retractor. In two experiments ( N = 151, N = 146), informant credibility and retractor credibility were independently manipulated. Participants read a fictitious news report in which original information and a retraction were each presented by either a source with high credibility or a source with low credibility. In both experiments, when the informant was more credible than the retractor, participants showed a CIE compared to control participants who saw neither the information nor the retraction ( d s > 0.82). When the informant was less credible than the retractor, participants showed no CIE, in line with a rational account. However, in Experiment 2, participants also showed a CIE when informant and retractor were equally credible ( d s > 0.51). This cannot be explained by a rational account, but is consistent with error-based accounts of the CIE. Thus, a rational account alone cannot fully account for the complete pattern of results, but needs to be complemented with accounts that view the CIE as a memory-based error. • Relative credibility of contradicting sources antagonistically affected the CIE. • Higher credibility of the source of the original information amplified the CIE. • Higher credibility of the source presenting the retraction attenuated the CIE. • Effects of relative source credibility on the CIE are in part rational. • The best explanation is a combination of rational processes and memory error.",
  "reason": "Dois experimentos (N = 151, N = 146) com notícia fictícia e credibilidade relativa de informante e retrator."
 },
 {
  "id": "C22",
  "title": "Does explaining the origins of misinformation improve the effectiveness of a given correction?",
  "year": 2022,
  "venue": "Memory & Cognition",
  "abstract": "Misinformation often has a continuing influence on event-related reasoning even when it is clearly and credibly corrected; this is referred to as the continued influence effect. The present work investigated whether a correction's effectiveness can be improved by explaining the origins of the misinformation. In two experiments, we examined whether a correction that explained misinformation as originating either from intentional deception or an unintentional error was more effective than a correction that only identified the misinformation as false. Experiment 2 found no evidence that corrections explaining the reason the misinformation was presented, were more effective than a correction not accompanied by an explanation, and no evidence of a difference in effectiveness between a correction that explained the misinformation as intentional deception and one that explained it as unintentional error. We replicated this in Experiment 2 and found substantial attenuation of the continued influence effect in a novel scenario with the same underlying structure. Overall, the results suggest that informing people of the cause leading to presentation of misinformation, whether deliberate or accidental, may not be an effective correction strategy over and above stating that the misinformation is false.",
  "reason": "Dois experimentos sobre explicar a origem da desinformação e a eficácia da correção no CIE."
 },
 {
  "id": "C23",
  "title": "Don’t believe them! Reducing misinformation influence through source discreditation",
  "year": 2024,
  "venue": "Cognitive Research Principles and Implications",
  "abstract": "Misinformation often continues to influence people's reasoning even after it has been corrected. Therefore, an important aim of applied cognition research is to identify effective measures to counter misinformation. One frequently recommended but hitherto insufficiently tested strategy is source discreditation, that is, attacking the credibility of a misinformation source. In two experiments, we tested whether immediate source discreditation could reduce people's subsequent reliance on fictional event-related misinformation. In Experiment 1, the discreditation targeted a person source of misinformation, pointing to a conflict of interest. This intervention was compared with a commonly employed message-focused correction and a combination of correction and discreditation. The discreditation alone was effective, but less effective than a correction, with the combination of both most effective. Experiment 2 compared discreditations that targeted a person versus a media source of misinformation, pointing either to a conflict of interest or a poor track record of communication. Discreditations were effective for both types of sources, although track-record discreditations were less effective when the misinformation source was a media outlet compared to a person. Results demonstrate that continued influence of misinformation is shaped by social as well as cognitive factors and that source discreditation is a broadly applicable misinformation countermeasure.",
  "reason": "Dois experimentos com desacreditação da fonte e dependência de desinformação fictícia sobre eventos."
 },
 {
  "id": "C07",
  "title": "Do the protective effects last? The effectiveness of alternative + forewarning/inoculation techniques in reducing misinformation reliance and reliance regression in the continued influence effect procedure",
  "year": 2025,
  "venue": "Quarterly Journal of Experimental Psychology",
  "abstract": "The continued influence effect (CIE) refers to continued reliance on misinformation, even after it has been retracted. There are several techniques to counter it, such as forewarnings or presenting alternative explanations that can replace misinformation in knowledge or mental models of events. However, the existing research shows that they generally do not eliminate CIE, and their protective effects do not appear to be durable over time. In two experiments ( N = 441), we aimed to investigate the effectiveness of the alternative explanation technique and a combination of an alternative explanation and a forewarning (Experiment 1) or inoculation (Experiment 2) in both reducing CIE and the effect of increasing misinformation reliance over time, which is called belief regression. We found that an alternative reduced CIE while combining it with a forewarning or inoculation boosted this protective effect in the pretest. Nevertheless, the protective effect of the alternative + forewarning and inoculation techniques was not sustained, as shown by the fact that misinformation reliance increased for over 7 days, despite continued memory of the correction. A similar pattern, albeit with mixed evidence from Null Hypothesis Significance Testing (NHST) versus Bayesian analyses, was found for the alternative + inoculation technique. In the ‘Discussion’ section, we address issues such as the potential cognitive mechanisms of this effect. Despite all the similarities, given the difference in both methodology and results, we proposed that increased misinformation reliance over time in inferential reasoning should be attributed not to belief regression but to a phenomenon we refer to as reliance regression .",
  "reason": "Dois experimentos (N = 441) sobre alternativa, alerta ou inoculação e a persistência da dependência da desinformação."
 },
 {
  "id": "C01",
  "title": "Vaccination against misinformation: The inoculation technique reduces the continued influence effect",
  "year": 2022,
  "venue": "PLoS ONE",
  "abstract": "The continued influence effect of misinformation (CIE) is a phenomenon in which certain information, although retracted and corrected, still has an impact on event reporting, reasoning, inference, and decisions. The main goal of this paper is to investigate to what extent this effect can be reduced using the procedure of inoculation and how it can be moderated by the reliability of corrections’ sources. The results show that the reliability of corrections’ sources did not affect their processing when participants were not inoculated. However, inoculated participants relied on misinformation less when the correction came from a highly credible source. For this source condition, as a result of inoculation, a significant increase in belief in retraction, as well as a decrease in belief in misinformation was also found. Contrary to previous reports, belief in misinformation rather than belief in retraction predicted reliance on misinformation. These findings are of both great practical importance as certain boundary conditions for inoculation efficiency have been discovered to reduce the impact of the continued influence of misinformation, and theoretical, as they provide insight into the mechanisms behind CIE. The results were interpreted in terms of existing CIE theories as well as within the remembering framework , which describes the conversion from memory traces to behavioral manifestations of memory.",
  "reason": "Experimento sobre inoculação e CIE com correção e credibilidade da fonte, em material fictício."
 },
 {
  "id": "C09",
  "title": "Examining the role of information integration in the continued influence effect using an event segmentation approach",
  "year": 2022,
  "venue": "PLOS ONE",
  "abstract": "Misinformation regarding the cause of an event often continues to influence an individual’s event-related reasoning, even after they have received a retraction. This is known as the continued influence effect (CIE). Dominant theoretical models of the CIE have suggested the effect arises primarily from failures to retrieve the correction. However, recent research has implicated information integration and memory updating processes in the CIE. As a behavioural test of integration, we applied an event segmentation approach to the CIE paradigm. Event segmentation theory suggests that incoming information is parsed into distinct events separated by event boundaries, which can have implications for memory. As such, when an individual encodes an event report that contains a retraction, the presence of event boundaries should impair retraction integration and memory updating, resulting in an enhanced CIE. Experiments 1 and 2 employed spatial event segmentation boundaries in an attempt to manipulate the ease with which a retraction can be integrated into a participant’s mental event model. While Experiment 1 showed no impact of an event boundary, Experiment 2 yielded evidence that an event boundary resulted in a reduced CIE. To the extent that this finding reflects enhanced retrieval of the retraction relative to the misinformation, it is more in line with retrieval accounts of the CIE.",
  "reason": "Experimentos sobre segmentação de eventos e CIE com relatos de eventos fictícios."
 },
 {
  "id": "C08",
  "title": "Exploring factors that mitigate the continued influence of misinformation",
  "year": 2021,
  "venue": "Cognitive Research Principles and Implications",
  "abstract": "Abstract Background The term “continued influence effect” (CIE) refers to the phenomenon that discredited and obsolete information continues to affect behavior and beliefs. The practical relevance of this work is particularly apparent as we confront fake news everyday. Thus, an important question becomes, how can we mitigate the continued influence of misinformation? Decades of research have identified several factors that contribute to the CIE reduction, but few have reported successful elimination. Across three studies, we evaluated the relative contribution of three factors (i.e., targeting the misinformation, providing an alternative explanation, and relative importance of the misinformation content) to the reduction of the CIE. Results Across three studies and two different CIE measures, we found that alternative provision consistently resulted in CIE reduction. Furthermore, under certain conditions, the combination of alternative inclusion and direct targeting of misinformation in the correction statement resulted in successful elimination of the CIE, such that individuals who encountered that type of correction behaved similarly to baseline participants who never encountered the (mis)information. In contrast, under one CIE measure, participants who received correction statements that failed to include those elements referenced the (mis)information as frequently as baseline participants who never encountered a correction. Finally, we delineated several component processes involved in misinformation outdating and found that the extent of outdating success varied as a function of the causality of misinformation. Conclusions The damaging effects of fake news are undeniable, and the negative consequences are exacerbated in the digital age. Our results contribute to our understanding of how fake news persists and how we may begin to mitigate their effects.",
  "reason": "Três estudos sobre fatores que reduzem o CIE, com cenários de eventos."
 },
 {
  "id": "C14",
  "title": "Comparing the use of open and closed questions for Web-based measures of the continued-influence effect",
  "year": 2018,
  "venue": "Behavior Research Methods",
  "abstract": "Open-ended questions, in which participants write or type their responses, are used in many areas of the behavioral sciences. Although effective in the lab, they are relatively untested in online experiments, and the quality of responses is largely unexplored. Closed-ended questions are easier to use online because they generally require only single key- or mouse-press responses and are less cognitively demanding, but they can bias the responses. We compared the data quality obtained using open and closed response formats using the continued-influence effect (CIE), in which participants read a series of statements about an unfolding event, one of which is unambiguously corrected later. Participants typically continue to refer to the corrected misinformation when making inferential statements about the event. We implemented this basic procedure online (Exp. 1A, n = 78), comparing standard open-ended responses to an alternative procedure using closed-ended responses (Exp. 1B, n = 75). Finally, we replicated these findings in a larger preregistered study (Exps. 2A and 2B, n = 323). We observed the CIE in all conditions: Participants continued to refer to the misinformation following a correction, and their references to the target misinformation were broadly similar in number across open- and closed-ended questions. We found that participants' open-ended responses were relatively detailed (including an average of 75 characters for inference questions), and almost all responses attempted to address the question. The responses were faster, however, for closed-ended questions. Overall, we suggest that with caution it may be possible to use either method for gathering CIE data.",
  "reason": "Experimentos online sobre CIE com perguntas abertas e fechadas, e tamanhos de amostra informados."
 },
 {
  "id": "C04",
  "title": "The inhibitory impact of collaboration on the continued influence effect of misinformation",
  "year": 2024,
  "venue": "Frontiers in Psychology",
  "abstract": "The continued influence effect (CIE) of misinformation refers to the persistence of misinformation's impact on memory and inference even when individuals are aware of a retraction. This study examined whether collaborative processes affect the CIE and investigated the underlying mechanisms through three experiments. Experiment 1 explored the general impact of collaboration on the CIE. Experiment 2 further dissected collaboration into turn-taking and free collaboration conditions, assessing their effects on the CIE at various recall intervals. Building on these findings, Experiment 3 delved into the mechanisms driving the differential effects of turn-taking and free collaboration on misinformation correction. Results revealed that turn-taking collaboration consistently mitigates the CIE, while the effect of free collaboration on misinformation correction is moderated by recall time. This variation is attributed to differences in re-exposure, cross-cuing, and forgetting across collaboration types. The present study contributes empirical support to the Knowledge Revision Theory of the CIE.",
  "reason": "Três experimentos sobre colaboração e CIE, com medidas de memória e inferência após retratação."
 },
 {
  "id": "C21",
  "title": "Listening to misinformation while driving: Cognitive load and the effectiveness of (repeated) corrections.",
  "year": 2022,
  "venue": "Journal of Applied Research in Memory and Cognition",
  "abstract": "Corrected misinformation can continue to influence inferential reasoning. It has been suggested that such continued influence is partially driven by misinformation familiarity, and that corrections should therefore avoid repeating misinformation to avoid inadvertent strengthening of misconceptions. However, evidence for such familiarity-backfire effects is scarce. We tested whether familiarity backfire may occur if corrections are processed under cognitive load. Although misinformation repetition may boost familiarity, load may impede integration of the correction, reducing its effectiveness and therefore allowing a backfire effect to emerge. Participants listened to corrections that repeated misinformation while in a driving simulator. Misinformation familiarity was manipulated through the number of corrections. Load was manipulated through a math task administered selectively during correction encoding. Multiple corrections were more effective than a single correction; cognitive load reduced correction effectiveness, with a single correction entirely ineffective under load. This provides further evidence against familiarity-backfire effects and has implications for real-world debunking.",
  "reason": "Experimento com correções sob carga cognitiva e retorno ao uso da desinformação no raciocínio inferencial."
 },
 {
  "id": "C26",
  "title": "Correcting the unknown: Negated corrections may increase belief in misinformation",
  "year": 2021,
  "venue": "Applied Cognitive Psychology",
  "abstract": "Summary Corrections are not always effective at reducing belief in misinformation. Negated corrections, which state a piece of information is not true, may only be effective at inhibiting information an observer has already encountered. We compared the effectiveness of negated corrections and replacements while manipulating initial exposure to a target concept. Subjects read one (Experiment 1) or six (Experiment 2) passages presenting a target concept (e.g., blue car) or not, followed by a negated correction (e.g., not blue), replacement (e.g., red), or no correction, then answered open‐ended questions which were scored for mentions of the target concept. When subjects were exposed to the target concept, negated corrections reduced mentions of the misinformation relative to no correction; however, when not exposed to the concept, negated corrections increased mentions relative to no correction. These results demonstrate that negated corrections can increase belief in misinformation when observers have not been exposed to the misinformation.",
  "reason": "Dois experimentos com correções negadas e menções à desinformação em passagens neutras."
 },
 {
  "id": "C02",
  "title": "Does Mud Really Stick? No Evidence for Continued Influence of Misinformation on Newly Formed Person Impressions",
  "year": 2024,
  "venue": "Collabra: Psychology",
  "abstract": "Despite robust evidence that misinformation continues to influence event-related reasoning after a clear retraction, evidence for the continued influence of misinformation on person impressions is mixed. Across four experiments, we investigated the impact of person-related misinformation and its correction on dynamic (moment-to-moment) impression formation. Participants formed an impression of a protagonist, “John”, based on a series of behaviour descriptions, including misinformation that was later retracted. Person impressions were recorded after the presentation of each behaviour description. As predicted, we found a strong effect of information valence on person impressions: negative misinformation had a greater impact on person impressions than positive misinformation (Experiments 1 and 2). Furthermore, in each experiment participants fully discounted the misinformation once retracted, regardless of whether the misinformation was negative or positive. This was true even when the other behaviour descriptions were congruent with (Experiment 2) or causally related to the retracted misinformation (Experiments 3 and 4). To test for generalisation, Experiment 4 used a different misinformation statement; it again showed no evidence for the continued influence of retracted misinformation on person impressions. Our findings indicate that person-related misinformation can be effectively discounted following a clear retraction.",
  "reason": "Quatro experimentos com retratação de desinformação sobre uma pessoa fictícia, medindo a influência continuada nas impressões."
 },
 {
  "id": "C18",
  "title": "Did he or didn’t he? Mixed evidence for the continued influence of retracted misinformation on person impressions",
  "year": 2025,
  "venue": "PLOS One",
  "abstract": "Retracted misinformation often continues to influence event-related reasoning, but there is mixed evidence that it influences person impressions. A recent study found no evidence for the continued influence of retracted misinformation on person impressions across four experiments. However, the study used a dynamic impression-rating measure that may have obscured any continued influence effects. Here we report three experiments that tested for the continued influence of retracted misinformation on person impressions using a non-dynamic impression-formation task that is comparable to tasks used in event-related misinformation research. Participants formed an impression of a fictitious person based on a series of behaviour statements. A negative behaviour statement (e.g., “John kicked his pet dog hard in the head when it didn’t come when called”) was subsequently retracted or not retracted. Evidence for the continued influence of the retracted behaviour statement was found in one experiment; in the other two experiments the retracted misinformation was fully discounted. The mixed findings indicate that, unlike retracted event-related misinformation, retracted person-related misinformation does not consistently show a continued influence effect. Future research should investigate potential moderating factors, such as the attributes of the misinformation and the presence of social-category information about the protagonist, to reveal the mechanisms underlying the continued influence effect in person impressions.",
  "reason": "Três experimentos com retratação de uma afirmação sobre uma pessoa fictícia e CIE."
 },
 {
  "id": "C46",
  "title": "Do false allegations persist? Retracted misinformation does not continue to influence explicit person impressions.",
  "year": 2020,
  "venue": "Journal of Applied Research in Memory and Cognition",
  "abstract": "Corrected misinformation often continues to influence reasoning; this is known as the continued-influence effect (CIE). It is unclear whether this effect also occurs in impression formation, with some arguing that person impressions are readily updated. The present study tested if a retracted allegation influences person impressions. Participants received examples of behaviors that a fictitious person had allegedly engaged in. The set did or did not include a domestic-violence behavior, which subsequently was or was not retracted. Discredited misinformation was found to influence neither trait ratings of the person nor behavior predictions. This held even when the person's name implied a cultural background stereotypically associated with domestic violence. This provides evidence that under some circumstances, people can fully discount discredited misinformation when building person impressions. However, there was some tentative evidence that corrected misinformation did influence a more indirect measure, namely ratings of the fictitious person's face.",
  "reason": "Experimento sobre uma alegação retratada e impressões de uma pessoa fictícia."
 },
 {
  "id": "C03",
  "title": "Electrophysiological correlates of the continued influence effect of misinformation: an exploratory study",
  "year": 2020,
  "venue": "Journal of Cognitive Psychology",
  "abstract": "Misinformation often affects inferential reasoning even after it has been retracted, known as the continued influence effect (CIE). Previous behavioural research into the effect’s underlying mechanisms has focussed on the role of long-term memory processes at the time misinformation is retrieved during inferential reasoning. We present the first investigation into the CIE using event-related potentials (ERPs). Participants completed a continued-influence task whilst electroencephalographic data were recorded. Analysis was guided by previous ERP research investigating post-event misinformation effects. ERPs elicited for retracted misinformation were more negative at a frontal-midline region of interest (300–500 ms) and more positive at a left-parietal region (450–600 ms) compared to correctly-accepted true information, though no differences were observed between rejected and accepted misinformation. This suggests that post-retraction reliance on misinformation may be driven by particularly strong recollection of the misinformation, ostensibly following poor integration of the retraction into the initial, partially invalid mental model.",
  "reason": "Estudo de ERP com tarefa de CIE e raciocínio inferencial após retratação, com participantes humanos."
 },
 {
  "id": "C13",
  "title": "Executive function and the continued influence of misinformation: A latent-variable analysis",
  "year": 2023,
  "venue": "PLoS ONE",
  "abstract": "Misinformation can continue to influence reasoning after correction; this is known as the continued influence effect (CIE). Theoretical accounts of the CIE suggest failure of two cognitive processes to be causal, namely memory updating and suppression of misinformation reliance. Both processes can also be conceptualised as subcomponents of contemporary executive function (EF) models; specifically, working-memory updating and prepotent-response inhibition. EF may thus predict susceptibility to the CIE. The current study investigated whether individual differences in EF could predict individual differences in CIE susceptibility. Participants completed several measures of EF subcomponents, including those of updating and inhibition, as well as set shifting, and a standard CIE task. The relationship between EF and CIE was then assessed using a correlation analysis of the EF and CIE measures, as well as structural equation modelling of the EF-subcomponent latent variable and CIE latent variable. Results showed that EF can predict susceptibility to the CIE, especially the factor of working-memory updating. These results further our understanding of the CIE's cognitive antecedents and provide potential directions for real-world CIE intervention.",
  "reason": "Estudo de variáveis latentes que usa tarefa padrão de CIE e funções executivas, com participantes humanos."
 },
 {
  "id": "C80",
  "title": "Sensitivity to misinformation retractions in the continued influence paradigm: Evidence for stability",
  "year": 2021,
  "venue": "Quarterly Journal of Experimental Psychology",
  "abstract": "Research has consistently shown that misinformation can continue to affect inferential reasoning after a correction. This phenomenon is known as the continued influence effect (CIE). Recent studies have demonstrated that CIE susceptibility can be predicted by individual differences in stable cognitive abilities. Based on this, it was reasoned that CIE susceptibility ought to have some degree of stability itself; however, this has never been tested. The current study aimed to investigate the temporal stability of retraction sensitivity, arguably a major determinant of CIE susceptibility. Participants were given parallel forms of a standard CIE task 4 weeks apart, and the association between testing points was assessed with an intra-class correlation coefficient and confirmatory factor analysis. Results suggested that retraction sensitivity is relatively stable and can be predicted as an individual-differences variable. These results encourage continued individual-differences research on the CIE and have implications for real-world CIE intervention.",
  "reason": "Participantes fizeram duas formas paralelas de uma tarefa de CIE com quatro semanas de intervalo, medindo a estabilidade da sensibilidade à retratação."
 },
 {
  "id": "C16",
  "title": "How Stories in Memory Perpetuate the Continued Influence of False Information",
  "year": 2019,
  "venue": "Journal of Consumer Psychology",
  "abstract": "People often encounter information that they subsequently learn is false. Past research has shown that people sometimes continue to use this misinformation in their reasoning, even if they remember that the information is false, which researchers refer to as the continued influence effect . The current work shows that the continued influence effect depends on the stories people have in memory: corrected misinformation was found to have a stronger effect on people's beliefs than information that was topically related to the story if it helped to provide a causal explanation of a story they had read previously. We argue this effect occurs because information that can fill a causal “gap” in a story enhances comprehension of the story event, which allows people to build a complete (if inaccurate) event model that they prefer over an accurate but incomplete event model. This effect is less likely to occur for stories in memory that end in a negative way, presumably because people are more motivated to accurately understand negative outcome events.",
  "reason": "Experimentos sobre histórias na memória e a influência continuada de informação corrigida."
 },
 {
  "id": "C29",
  "title": "Not wallowing in misery – retractions of negative misinformation are effective in depressive rumination",
  "year": 2018,
  "venue": "Cognition & Emotion",
  "abstract": "People often continue to rely on misinformation in their reasoning after they have acknowledged a retraction; this phenomenon is known as the continued-influence effect. Retractions can be particularly ineffective when the retracted misinformation is consistent with a pre-existing worldview. We investigated this effect in the context of depressive rumination. Given the prevalence of depressotypic worldviews in depressive rumination, we hypothesised that depressive rumination may affect the processing of retractions of valenced misinformation; specifically, we predicted that the retraction of negative misinformation might be less effective in depressive ruminators. In two experiments, we found evidence against this hypothesis: in depressive ruminators, retractions of negative misinformation were at least as effective as they were in control participants, and more effective than retractions of positive misinformation. Findings are interpreted in terms of an attentional bias that may enhance the salience of negative misinformation and may thus facilitate its updating in depressive rumination.",
  "reason": "Dois experimentos sobre retratação de desinformação em ruminação depressiva, com relatos de eventos fictícios."
 },
 {
  "id": "C30",
  "title": "The continued influence of implied and explicitly stated misinformation with different emotional valence",
  "year": 2024,
  "venue": "Journal of Cognitive Psychology",
  "abstract": "Misinformation often affects people’s cognition and judgment even when they are aware of a retraction; this is known as the continued influence effect of misinformation (CIE). The aim of the present study was to verify if the expressive style affects the CIE with different emotional valence. We designed a 2 (emotional valence: positive or negative) * 2(expressive style: explicit or implied) * 2 (correction condition: uncorrected or corrected) within-subject experiment. Participants were asked to finish memory questions and inference questions. The results found an interaction between expressive style and emotional valence. For positive misinformation, the expressive style had no effect; for negative misinformation, the CIE was stronger in the explicitly stated condition compared with the implied condition. The explicitly stated misinformation was more difficult to correct than the implied misinformation. The results provided evidence to explain the role of emotional valence and expressive style on CIE.",
  "reason": "Experimento sobre CIE com estilo de expressão e valência emocional, com medidas de memória e inferência."
 },
 {
  "id": "C42",
  "title": "Reading Medium and Epistemic Emotions in the Continued Influence Effect of Misinformation",
  "year": 2024,
  "venue": "Reading Psychology",
  "abstract": "It is well known that misinformation’s effects on memory linger, referred to as the continued influence effect, even after reading corrections. However, it is uncertain how the reading medium and epistemic emotions (relevant to knowledge construction) relate to the continued influence effect. In this study, college students (N = 84) read about fictional news events, each with the first article stating misinformation and the second providing corrected updated information, on paper and on screen and then indicated their emotions experienced in a within-subjects experiment. There were no reliable differences in the continued misinformation effect by reading medium. However, the associations between epistemic emotions and misinformation ratings appeared to be more robust when reading from paper than screens. There were no reliable differences in epistemic emotions experienced by reading medium. The findings indicate that reading news online does not appear to relate to susceptibility of misinformation.",
  "reason": "Experimento (N = 84) com notícias fictícias corrigidas e CIE por meio de leitura."
 },
 {
  "id": "C43",
  "title": "Influence of individual differences in executive functions of WM on the continued influence effect of misinformation",
  "year": 2023,
  "venue": "Journal of Cognitive Psychology",
  "abstract": "Misinformation often affects people’s cognition and judgment even when they are aware of a retraction; this is known as the continued influence effect of misinformation (CIE). The aim of the present study was to verify if there were differences in the continued influence effect with respect to the individual’s EF availability of WM (i.e. inhibition, shifting and updating). The Stroop task, number shifting task and the n-back task were adopted to investigate the three executive functions of inhibition, shifting and updating, respectively. The results showed that differences in inhibition, but not in shifting and updating, had a significant negative effect on the CIE. The continued effect of misinformation was lower for individuals with high function of inhibition. The current study showed that high-inhibition individuals were less affected by the misinformation. The study extends our understanding of the relationship between executive functions and the CIE.",
  "reason": "Estudo sobre diferenças individuais de funções executivas e CIE com tarefa de retratação."
 },
 {
  "id": "C94",
  "title": "Influence of individual differences in working memory on the continued influence effect of misinformation",
  "year": 2020,
  "venue": "Journal of Cognitive Psychology",
  "abstract": "Misinformation often continues to influence people’s cognition even after being retracted (the continued influence effect of misinformation, CIE). The current research aimed to investigate whether the individual differences in the central executive function of WM and updating could influence the CIE of misinformation with varying relevance. The results showed that the individual differences in central executive function could significantly affect the CIE, especially for the high-relevant misinformation. While the individual differences in the updating ability had a weaker impact on the CIE in general and only negatively related to the CIE for the low-relevant misinformation. The study extends the understanding of the relationship between individual differences and the CIE from previous studies, which is in line with the mental-model-updating hypothesis, and offers a preliminary clue for identifying the persons vulnerable to the CIE of misinformation in the real world.",
  "reason": "Estudo sobre memória de trabalho e CIE com desinformação de relevância variada."
 },
 {
  "id": "C40",
  "title": "Combating false information in military situations: Striking the right balance between continued influence effect and overcorrection",
  "year": 2024,
  "venue": "Applied Cognitive Psychology",
  "abstract": "Abstract False information (FI) is a critical issue for the military, and correction is a common strategy to counteract its influence. However, literature questions the potential of correction to fully restore optimal reasoning. Some studies suggest an overcorrection effect, aligning attitudes excessively with the correction, while others highlight the continued influence effect (CIE), where attitudes persist in alignment with FI. This research aimed to examine the effect of an FI correction within military scenarios. A total of 61 participants read four military scenarios designed to simulate decision‐making, followed by an assessment of their inferential reasoning. Two of the scenarios presented FI which was later retracted, and the two remaining scenarios did not. The results did not reveal any evidence of the CIE, but an overcorrection effect emerged in decision‐making. The study underscores an underestimated threat in countering misinformation. The theoretical and practical implications are discussed.",
  "reason": "Experimento (N = 61) com cenários militares fictícios e informação falsa retratada."
 }
]