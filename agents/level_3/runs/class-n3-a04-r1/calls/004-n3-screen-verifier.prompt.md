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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre jogos educativos e jogos de inoculação (prebunking) contra desinformação, como o Bad News. Restrições: apenas intervenções em forma de jogo (digital ou de tabuleiro) avaliadas com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção; exclua intervenções que não são jogos (vídeos, textos ou infográficos isolados), reanálises de dados de outros estudos e estudos centrados em COVID-19, vacinas, eleições ou política partidária (por exemplo, o Go Viral!). Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CRITÉRIOS:
{
 "include": [
  "Artigo de periódico revisado por pares com estudo empírico e dados próprios",
  "Publicado entre 2018 e 2025",
  "A intervenção é um jogo (digital, online ou de tabuleiro) voltado a desinformação, fake news, manipulação ou inoculação/prebunking (ex.: Bad News, Harmony Square, Cranky Uncle, Fake It to Make It, Factitious, Escape room educativo sobre desinformação)",
  "Avaliação com participantes em experimento, quase-experimento, ensaio randomizado ou desenho pré e pós-intervenção",
  "Desfechos relacionados à identificação de desinformação, resistência/imunidade, confiança, discernimento da verdade ou habilidades de checagem",
  "Tamanho da amostra identificável no resumo, ou registrar como não informado no resumo",
  "Resumo disponível com trecho que sustente o achado principal"
 ],
 "exclude": [
  "Intervenções que não são jogos (vídeos, textos, infográficos, anúncios, dicas ou cursos isolados)",
  "Reanálises de dados de outros estudos ou análises secundárias",
  "Estudos centrados em COVID-19, vacinas, eleições ou política partidária (ex.: Go Viral!)",
  "Revisões de literatura, revisões sistemáticas e meta-análises",
  "Ensaios teóricos, conceituais ou de opinião, propostas de design de jogo sem avaliação com participantes",
  "Preprints",
  "Trabalhos de anais de congresso",
  "Capítulos de livro, livros, teses e dissertações",
  "Resenhas e editoriais",
  "Publicações fora do período 2018 a 2025",
  "Estudos sobre jogos sem relação com desinformação (ex.: jogos educativos de outros conteúdos)"
 ]
}

ARTIGOS INCLUÍDOS, COM O RESUMO BAIXADO POR CÓDIGO:
[
 {
  "id": "C01",
  "title": "Fake news game confers psychological resistance against online misinformation",
  "year": 2019,
  "venue": "Humanities and Social Sciences Communications",
  "abstract": "Abstract The spread of online misinformation poses serious challenges to societies worldwide. In a novel attempt to address this issue, we designed a psychological intervention in the form of an online browser game. In the game, players take on the role of a fake news producer and learn to master six documented techniques commonly used in the production of misinformation: polarisation, invoking emotions, spreading conspiracy theories, trolling people online, deflecting blame, and impersonating fake accounts. The game draws on an inoculation metaphor, where preemptively exposing, warning, and familiarising people with the strategies used in the production of fake news helps confer cognitive immunity when exposed to real misinformation. We conducted a large-scale evaluation of the game with N = 15,000 participants in a pre-post gameplay design. We provide initial evidence that people’s ability to spot and resist misinformation improves after gameplay, irrespective of education, age, political ideology, and cognitive style.",
  "reason": "Jogo Bad News avaliado em desenho pré e pós com N = 15.000."
 },
 {
  "id": "C12",
  "title": "Good News about Bad News: Gamified Inoculation Boosts Confidence and Cognitive Immunity Against Fake News",
  "year": 2020,
  "venue": "Journal of Cognition",
  "abstract": "Recent research has explored the possibility of building attitudinal resistance against online misinformation through psychological inoculation. The inoculation metaphor relies on a medical analogy: by pre-emptively exposing people to weakened doses of misinformation cognitive immunity can be conferred. A recent example is the Bad News game, an online fake news game in which players learn about six common misinformation techniques. We present a replication and extension into the effectiveness of Bad News as an anti-misinformation intervention. We address three shortcomings identified in the original study: the lack of a control group, the relatively low number of test items, and the absence of attitudinal certainty measurements. Using a 2 (treatment vs. control) × 2 (pre vs. post) mixed design (N = 196) we measure participants’ ability to spot misinformation techniques in 18 fake headlines before and after playing Bad News. We find that playing Bad News significantly improves people’s ability to spot misinformation techniques compared to a gamified control group, and crucially, also increases people’s level of confidence in their own judgments. Importantly, this confidence boost only occurred for those who updated their reliability assessments in the correct direction. This study offers further evidence for the effectiveness of psychological inoculation against not only specific instances of fake news, but the very strategies used in its production. Implications are discussed for inoculation theory and cognitive science research on fake news.",
  "reason": "Bad News com grupo controle em desenho 2×2, N = 196."
 },
 {
  "id": "C08",
  "title": "Technique-based inoculation against real-world misinformation",
  "year": 2022,
  "venue": "Royal Society Open Science",
  "abstract": "In recent years, numerous psychological interventions have been developed to reduce susceptibility to misinformation. Inoculation theory has become an increasingly common framework for reducing susceptibility to both individual examples of misinformation (issue-based inoculation) and to the techniques and strategies that are commonly used to mislead or misinform people (technique-based inoculation). In this study, we address two open questions related to technique-based inoculation in two separate experiments (total n = 2188; convenience sample recruited via the Bad News online game platform): (i) can technique-based inoculation effectively reduce susceptibility to real-world misinformation that went viral on social media? and (ii) can technique-based inoculation confer cross-protection against misinformation that does not make use of any of the techniques against which people were inoculated? We find that playing a 15 min game confers psychological resistance against real-world misinformation that makes use of manipulation techniques against which people were inoculated (Cohen's d = 0.37, Cohen's U 3 = 64.4%, p &lt; 0.001), and that cross-protection is achieved but at a reduced effect size ( d = 0.10, U 3 = 54.0%, p = 0.001).",
  "reason": "Dois experimentos com o jogo Bad News, n total = 2188."
 },
 {
  "id": "C09",
  "title": "Prebunking interventions based on the psychological theory of “inoculation” can reduce susceptibility to misinformation across cultures.",
  "year": 2020,
  "venue": "Harvard Kennedy School Misinformation Review",
  "abstract": "This study finds that the online “fake news” game, Bad News, can confer psychological resistance against common online misinformation strategies (e.g., conspiracy theories, manipulating emotions, political polarization) across different cultures (Sweden, German, Poland, and Greece). The intervention draws on the theory of psychological inoculation: analogous to the process of medical immunization, we find that “prebunking” or preemptively warning and exposing people to weakened doses of misinformation can help cultivate “mental antibodies” against fake news. We conclude that social impact games rooted in basic insights from social psychology can boost immunity against misinformation across a variety of cultural, linguistic, and political settings.",
  "reason": "Bad News testado em quatro países. O resumo não informa a amostra."
 },
 {
  "id": "C21",
  "title": "Disentangling Item and Testing Effects in Inoculation Research on Online Misinformation: Solomon Revisited",
  "year": 2020,
  "venue": "Educational and Psychological Measurement",
  "abstract": "Online misinformation is a pervasive global problem. In response, psychologists have recently explored the theory of psychological inoculation: If people are preemptively exposed to a weakened version of a misinformation technique, they can build up cognitive resistance. This study addresses two unanswered methodological questions about a widely adopted online “fake news” inoculation game, Bad News. First, research in this area has often looked at pre- and post-intervention difference scores for the same items, which may imply that any observed effects are specific to the survey items themselves (item effects). Second, it is possible that using a pretest influences the outcome variable of interest, or that the pretest may interact with the intervention (testing effects). We investigate both item and testing effects in two online studies (total N = 2,159) using the Bad News game. For the item effect, we examine if inoculation effects are still observed when different items are used in the pre- and posttest. To examine the testing effect, we use a Solomon’s Three Group Design. We find that inoculation interventions are somewhat influenced by item effects, and not by testing effects. We show that inoculation interventions are effective at improving people’s ability to spot misinformation techniques and that the Bad News game does not make people more skeptical of real news. We discuss the larger relevance of these findings for evaluating real-world psychological interventions.",
  "reason": "Dois estudos com Bad News e desenho de Solomon, N = 2.159."
 },
 {
  "id": "C33",
  "title": "Feedback exercises boost discernment of misinformation for gamified inoculation interventions.",
  "year": 2024,
  "venue": "Journal of Experimental Psychology General",
  "abstract": "Gamification is a promising approach to reducing misinformation susceptibility. Previous research has found that \"inoculation\" games such as Bad News and Harmony Square help build cognitive resistance against misinformation. However, recent research has offered two important nuances: a potentially inadvertent impact of such games on people's evaluation of non-misinformation (\"real news\") and exponential decay over time if no memory-strengthening exercise is provided. We address these issues in two preregistered lab experiments (N1 = 191, N2 = 321) and four quasi-experimental in-game surveys implemented in Harmony Square (N3 = 559) and Bad News (N4 = 2,558, N5 = 419, N6 = 882). In Experiments 1 and 2, we test if providing different types of feedback after playing Bad News enhances discriminative ability of misinformation and real news 1 week postgameplay and find that doing so resulted in homogeneously better accuracy at identifying both misinformation and non-misinformation compared with a control condition, which played Bad News without feedback. In Experiments 3-6, we implemented two different types of feedback exercises in the Harmony Square and Bad News games and find that this significantly boosts discernment compared with playing the game without a feedback exercise, primarily by improving accuracy at detecting real news. We confirm these results using signal detection theory. We conclude that feedback exercises boost the effectiveness of gamified misinformation interventions, likely due to an improved learning environment. (PsycInfo Database Record (c) 2024 APA, all rights reserved).",
  "reason": "Experimentos com Bad News e Harmony Square, com feedback após o jogo. Amostras de 191 a 2.558."
 },
 {
  "id": "C38",
  "title": "Bad News in the civics classroom: How serious gameplay fosters teenagers’ ability to discern misinformation techniques",
  "year": 2024,
  "venue": "Journal of Research on Technology in Education",
  "abstract": "Although the serious game Bad News has been used to inoculate citizens against misinformation, it has not been formally evaluated in traditional classrooms. We therefore evaluated its impact on 516 upper-secondary Swedish students playing individually, paired, or with the whole class. Results show that students improved their ability to discern manipulation techniques in social media posts. Students with prior positive attitudes to credible news sources were better discerners, and this attitude became significantly more positive post-intervention. Rationales for identifying manipulative techniques increased among those who improved their credibility ratings pre-to post-intervention. Lastly, enjoyment of and interest in the intervention was higher in the whole-class setting. This study offers insights for educators on using serious games in formal teaching to foster media and information literacy.",
  "reason": "Bad News aplicado em sala de aula, com 516 estudantes."
 },
 {
  "id": "C03",
  "title": "Breaking Harmony Square: A game that “inoculates” against political misinformation",
  "year": 2020,
  "venue": "Harvard Kennedy School Misinformation Review",
  "abstract": "We present Harmony Square, a short, free-to-play online game in which players learn how political misinformation is produced and spread. We find that the game confers psychological resistance against manipulation techniques commonly used in political misinformation: players from around the world find social media content making use of these techniques significantly less reliable after playing, are more confident in their ability to spot such content, and less likely to report sharing it with others in their network.",
  "reason": "Jogo Harmony Square de inoculação, avaliado com participantes. O resumo não informa a amostra."
 },
 {
  "id": "C65",
  "title": "How to “inoculate” against multimodal misinformation: A conceptual replication of Roozenbeek and van der Linden (2020)",
  "year": 2023,
  "venue": "Scientific Reports",
  "abstract": "Building misinformation resilience at scale continues to pose a challenge. Gamified \"inoculation\" interventions have shown promise in improving people's ability to recognize manipulation techniques commonly used in misinformation, but so far few interventions exist that tackle multimodal misinformation (e.g., videos, images). We developed a game called Cat Park, in which players learn about five manipulation techniques (trolling, emotional manipulation, amplification, polarization, and conspiracism), and how misinformation can spread through images. To test the game's efficacy, we conducted a conceptual replication (N = 380) of Roozenbeek and van der Linden's 2020 study about Harmony Square, with the same study design, item set, and hypotheses. Like the original study, we find that people who play Cat Park find misinformation significantly less reliable post-gameplay (d = 0.95, p < 0.001) compared to a control group, and are significantly less willing to share misinformation with people in their network (d = 0.54, p < 0.001). These effects are robust across different covariates. However, unlike the original study, Cat Park players do not become significantly more confident in their ability to identify misinformation (p = 0.204, d = - 0.13). We did not find that the game increases people's self-reported motivation and confidence to counter misinformation online.",
  "reason": "Jogo Cat Park contra desinformação multimodal, N = 380."
 },
 {
  "id": "C06",
  "title": "Game-based inoculation versus graphic-based inoculation to combat misinformation: a randomized controlled trial",
  "year": 2023,
  "venue": "Cognitive Research Principles and Implications",
  "abstract": "Abstract Misinformation affects various aspects of people’s lives, such as politics, entertainment, and social interactions. However, effective intervention measures to combat misinformation are lacking. The inoculation theory has become a prevalent measure of misinformation. This study employed inoculation theory and developed an interactive game to help the public counter misinformation. In this game, players take on the role of the misinformation spreader, intending to add more followers to their virtual accounts using different strategies. A total of 180 Chinese participants were randomly assigned to game-based inoculation, graphic-based inoculation, and control groups. The results indicated that both types of inoculation interventions significantly decreased the perceived credibility and sharing intention of misinformation. Game-based inoculation was more effective than graphic-based inoculation in terms of misinformation perceived credibility, and the intervention effects were stable after 2 weeks. The graphic-based inoculation contained the sleeper effect, which interventions required a period of time to take effect. Neither inoculation produced countereffects on perceived credibility and nor sharing intention of accurate information.",
  "reason": "Ensaio randomizado com jogo de inoculação, N = 180."
 },
 {
  "id": "C05",
  "title": "Winning the game against fake news? Using games to inoculate adolescents and young adults in Singapore against fake news",
  "year": 2023,
  "venue": "Estudios sobre el Mensaje Periodístico",
  "abstract": "Guided by inoculation theory and studies that examined serious games as a form of intervention to inoculate individuals against fake news, this study tested the impact on college (n = 84) and junior high and secondary school (n = 30) students of a fake news computer game developed in Singapore. The findings were replicated across both samples: Those who played the game subsequently improved in their self-reported scores on perceiving fake news as a threat, skepticism toward information from social media, and being cautious about believing in information they encounter online. We also found that those who played the game scored higher in detecting fake news than those who did not play the game–consistent with the predicted effects of message inoculation.",
  "reason": "Jogo contra fake news testado em estudantes (n = 84 e n = 30), com comparação entre quem jogou e quem não jogou."
 },
 {
  "id": "C43",
  "title": "Inoculation against conspiracy theories: A consumer side approach to India's fake news problem",
  "year": 2022,
  "venue": "Applied Cognitive Psychology",
  "abstract": "Abstract We attempt to replicate Roozenbeek and van der Linden's Western‐based study in India by employing the Bad News Game , an online game, in which players take on the role of a misinformation tycoon. They are exposed to weakened doses of the strategies employed in conspiracy and fake news production with the aim to cognitively inoculate them against misinformation. The proliferation of inexpensive mobile connections coupled with a lack of digital literacy has resulted in a conspiratorial pandemic in developing countries like India. We test the game's impact on an Indian sample ( n = 1002) using a within‐subject design. We provide evidence of significant improvement in the ability of participants to identify the misinformation produced using Conspiracy , Impersonation , and to a lesser extent, the Discrediting technique, while observing greater truth discernment in correctly identifying true news. We also conduct sub‐sample analyses. These findings have positive implications for methods that protect users from malignant online content.",
  "reason": "Bad News aplicado na Índia, n = 1002, com desenho intrassujeito."
 },
 {
  "id": "C14",
  "title": "Gamified Inoculation Against Misinformation in India: A Randomized Control Trial",
  "year": 2023,
  "venue": "Journal of Trial and Error",
  "abstract": "Although the spread of misinformation is a pervasive and disruptive global problem, extant research is skewed towards “WEIRD” countries leaving questions about how to tackle misinformation in the developing world with different media and consumption patterns unanswered. We report the results of a game-based intervention against misinformation in India. The game is based on the mechanism of psychological inoculation; borrowed from the medical context, inoculation interventions aim to pre-emptively neutralize falsehoods and help audiences spot and resist misinformation strategies. Though the efficacy of these games has been repeatedly demonstrated in samples from Western countries, the present study conducted in north India (n = 757) did not replicate earlier findings. We found no significant impact of the intervention on the perceived reliability of messages containing misinformation, confidence judgments, and willingness to share information with others. Our experience presents a teachable moment for the unique challenges associated with complex cultural adaptations and field work in rural areas. These results have significant ramifications for designing misinformation interventions in developing countries where misinformation is largely spread via encrypted messaging applications such as WhatsApp. Our findings contribute to the small but growing body of work looking at how to adapt misinformation interventions to cross-cultural settings.",
  "reason": "Ensaio randomizado de jogo de inoculação na Índia, n = 757. O resultado foi nulo, mas o estudo atende aos critérios."
 },
 {
  "id": "C07",
  "title": "Re-examining the bad news game: No evidence of improved discrimination of Indian true and fake news headlines",
  "year": 2025,
  "venue": "Psychonomic Bulletin & Review",
  "abstract": "Abstract Gamified inoculation interventions such as the Bad News game are a widely adopted approach to mitigating the influence of misinformation. While Bad News has been predominately studied with participants from Western, Educated, Industrialized, and Rich Democracies (WEIRD), one recent study (Iyengar et al., Applied Cognitive Psychology, 37:290–303, 2023) assessed its efficacy in an Indian sample. In that study, participants rated the reliability of a series of Indian news headlines in a pre-test, played Bad News, and completed a post-test with a different set of headlines. Participants showed better discrimination of true and fake headlines in the post-test than the pre-test. This finding contrasts with a meta-analysis showing that Bad News primarily produces a conservative response bias rather than improving discrimination (Modirrousta-Galian and Higham, Journal of Experimental Psychology: General , 152:2411–2437, 2023). The current preregistered study used the same design as Iyengar et al., although participants of Indian nationality ( N = 150) were recruited via Prolific and the allocation of news headlines to the pre-test and post-test was counterbalanced. When both counterbalancing conditions were included, no significant differences in discrimination or response bias appeared between the pre-test and post-test. When only the counterbalancing condition matching Iyengar et al.’s experiment was examined, no significant effect on discrimination was observed, but a conservative response bias shift was seen in the post-test. This finding suggests that the Bad News game may be less effective for improving discrimination than previously thought – an important consideration given its popularity as an intervention to combat misinformation.",
  "reason": "Estudo pré-registrado com dados novos (N = 150) sobre o Bad News. Não é reanálise."
 },
 {
  "id": "C42",
  "title": "Mixed News about the Bad News Game",
  "year": 2023,
  "venue": "Journal of Cognition",
  "abstract": "Basol et al. (2020) tested the \"the Bad News Game\" (BNG), an app designed to improve ability to spot false claims on social media. Participants rated simulated Tweets, then played either the BNG or an unrelated game, then re-rated the Tweets. Playing the BNG lowered rated belief in false Tweets. Here, four teams of undergraduate psychology students each attempted an extended replication of Basol et al., using updated versions of the original Bad News game. The most important extension was that the replications included a larger number of true Tweets than the original study and planned analyses of responses to true Tweets. The four replications were loosely coordinated, with each team independently working out how to implement the agreed plan. Despite many departures from the Basol et al. method, all four teams replicated their key finding: Playing the BNG reduced belief in false Tweets. But playing the BNG also reduced belief in true Tweets to the same or almost the same extent. Exploratory signal detection theory analyses indicated that the BNG increased response bias but did not improve discrimination. This converges with findings reported by Modirrousta-Galian and Higham (2023).",
  "reason": "Quatro replicações com dados novos do Bad News. O resumo não informa a amostra."
 },
 {
  "id": "C103",
  "title": "Effects of inductive learning and gamification on news veracity discernment.",
  "year": 2023,
  "venue": "Journal of Experimental Psychology Applied",
  "abstract": "= 282 Prolific users) were randomly assigned to either a gamified IL intervention, a nongamified version of the same IL intervention, a no-treatment control group, or a Bad News intervention, a notable web-based game designed to tackle online misinformation. Following the intervention (if applicable), all participants rated the veracity of a novel set of news headlines. We hypothesized that the gamified intervention would be the most effective for improving news veracity discernment, followed by its nongamified equivalent, then Bad News, and finally the control group. The results were analyzed with receiver-operating characteristic curve analyses, which have previously never been applied to news veracity discernment. The analyses indicated that there were no significant differences between conditions and the Bayes factor indicated very strong evidence for the null. This finding raises questions about the effectiveness of current psychological interventions and contradicts prior research that has supported the efficacy of Bad News. Age, gender, and political leaning all predicted news veracity discernment. (PsycInfo Database Record (c) 2023 APA, all rights reserved).",
  "reason": "Experimento randomizado que compara intervenção gamificada e Bad News, N = 282."
 },
 {
  "id": "C30",
  "title": "Gamified inoculation reduces susceptibility to misinformation from political ingroups",
  "year": 2024,
  "venue": "Harvard Kennedy School Misinformation Review",
  "abstract": "Psychological inoculation interventions, which seek to pre-emptively build resistance against unwanted persuasion attempts, have shown promise in reducing susceptibility to misinformation. However, as many people receive news from popular, mainstream ingroup sources (e.g., a left-wing person consuming left-wing media) which may host misleading or false content, and as ingroup sources may be more persuasive, the impact of source effects on inoculation interventions demands attention. In this experiment, we find that although news consumers are more susceptible to (non-political) misinformation from political ingroup publishers pre-intervention, gamified inoculation successfully improves veracity discernment and reduces susceptibility to misinformation from both political ingroup and outgroup publishers.",
  "reason": "Experimento com inoculação gamificada. A desinformação avaliada não é política e o resumo não informa a amostra."
 },
 {
  "id": "C13",
  "title": "MAthE the Game: A Serious Game for Education and Training in News Verification",
  "year": 2019,
  "venue": "Education Sciences",
  "abstract": "During the last years, there has been a growing multidisciplinary interest in alternative educational approaches, such as serious games, aiming at enhancing thinking skills and media literacy. Likewise, the objective of this study is to present the design and the development of an educational web application for learning the necessary steps towards the detection of bogus content, according to the fact-checking procedures. The game presents news articles, which have to be characterized as fake or real by the players. During the effort to reach the correct decision, the players can use tools and practices for identifying relevant information regarding the clues, which frame a news story (title, date, creator, source, containing images). After presenting the progress of interface design and development, this paper reports the results of a randomized online field study (n = 111), which provides some preliminary evidence. Specifically, it is validated that the game can raise awareness, teach about authentication tools, and highlight the importance of patterns that include evidence regarding the authenticity of articles. Additionally, thorough discussion was conducted within a media class (n = 35) to receive useful feedback/evaluation about the offered utilities and their usability. The findings suggest that educational games may be a promising vehicle to inoculate the public against misinformation.",
  "reason": "Jogo sério de verificação de notícias avaliado em estudo de campo randomizado, n = 111."
 },
 {
  "id": "C23",
  "title": "Enhancing Information Literacy for Spotting Fake News: A Study on the Efficacy of a Serious Game for M-Learning Across Different Age Groups",
  "year": 2023,
  "venue": "International Journal of Interactive Mobile Technologies (iJIM)",
  "abstract": "With so many online information sources in recent years, it has become increasingly difficultto determine if the content is based on facts, half-truths, or lies. As a result, the goal of thisresearch is to propose a serious game design for learning to evaluate sources using the CRAAPtest. In the game, players take on the role of librarians who must evaluate news from socialmedia and newspapers, determine whether it is fake or true, and then inform the people ofthe city. During their efforts to make the correct decision, the players are able to observe andlearn about the impact of fake news on the community and the city as a result of their decisions.To evaluate the game, we did a randomized online field study, including quantitativeresearch based on pre-posttests involving 351 participants. The results revealed that using aserious game of “How to Spot Fake News” can improve the knowledge of information literacyneeded to evaluate online sources of information. Finally, we provide preliminary evidencethat gaming improves people’s ability to recognize and resist misinformation.",
  "reason": "Jogo sério avaliado em estudo de campo randomizado com pré e pós-teste, 351 participantes."
 },
 {
  "id": "C28",
  "title": "Effekte eines Augmented Reality Escape Games auf das Lernen über Fake News Effects of an Augmented Reality Escape Game on Learning about Fake News",
  "year": 2023,
  "venue": "MedienPädagogik: Zeitschrift für Theorie und Praxis der Medienbildung",
  "abstract": "Die Verbreitung von Fake News im Internet und in sozialen Netzwerken schadet zunehmend dem gesellschaftlichen Zusammenleben, etwa indem das Vertrauen in demokratische Strukturen und Institutionen untergraben wird. Das Erkennen von Fake News ist schwierig, da Onlineinformationen mehr vertraut wird als klassischen Medien und Fake News emotionalisierend und vertrauenswürdig gestaltet werden. Um diesem Problem zu begegnen, braucht es authentische und innovative Bildungsangebote, die sowohl Wissen über Merkmale von Fake News vermitteln als auch eine kritischere Einstellung gegenüber Onlineinformationen fördern. In der bisherigen Forschung haben sich (digitale) Spiele hierfür als vielversprechend herausgestellt. In dieser Studie wird untersucht, ob auch ein Augmented-Reality-basiertes Escape Game Lernziele adressieren kann, die für den Unterricht über Fake News relevant sind. Um diese Frage zu beantworten, wurde ein Vortest-Nachtest Design mit 27 Schüler:innen durchgeführt. Wie die Ergebnisse zeigen, kann das untersuchte Spiel «Escape Fake» Wissen über Fake News vermitteln, die Fähigkeit fördern, die Zuverlässigkeit von Informationen zu erkennen, zu einer kritischeren Haltung gegenüber der Vertrauenswürdigkeit von Onlineinformationen beitragen sowie die Zuversicht stärken, auch in Zukunft Fake News zu erkennen. Auf der Basis der Ergebnisse dieser ersten Pilotstudie kann das Spiel als Bildungsressource für den Einsatz im Fake News-Unterricht empfohlen werden. Weitere Forschung ist jedoch notwendig, um die Effekte zu erklären und die Effektivität zu erhöhen.",
  "reason": "Escape game em realidade aumentada (Escape Fake) sobre fake news, com pré e pós-teste em 27 alunos."
 },
 {
  "id": "C75",
  "title": "Playing an Augmented Reality Escape Game Promotes Learning About Fake News",
  "year": 2024,
  "venue": "Technology, Knowledge and Learning",
  "abstract": "Abstract The spread of fake news poses a global challenge to society, as this deliberately false information reduce trust in democracy, manipulate opinions, and negatively affect people’s health. Educational research and practice must address this issue by developing and evaluating solutions to counter fake news. A promising approach in this regard is the use of game-based learning environments. In this study, we focus on Escape Fake , an augmented reality (AR) escape game developed for use in media literacy education. To date, there is limited research on the effectiveness of the game for learning about fake news. To overcome this gap, we conducted a field study using a pretest-posttest research design. A total of 28 students (14 girls, mean age = 14.71 years) participated. The results show that Escape Fake can address four learning objectives relevant in fake news detection with educationally desired effect sizes: Knowledge acquisition ( d = 1.34), ability to discern information ( d = 0.39), critical attitude toward trustworthiness of online information ( d = 0.53), and confidence in recognizing fake news in the future ( d = 0.41). Based on these results, the game can be recommended as an educational resource for media literacy education. Future research directions are also discussed.",
  "reason": "Escape Fake com pré e pós-teste em 28 estudantes."
 },
 {
  "id": "C32",
  "title": "Can pre-service teachers learn about fake news by playing an augmented reality escape game?",
  "year": 2024,
  "venue": "Contemporary Educational Technology",
  "abstract": "Fake news is increasingly becoming a major problem for global social coexistence, for example by undermining trust in democracies. There is a consensus that educational institutions need to respond and prepare students to recognize fake news. Teachers have a central role to play in preparing students and therefore need to learn about fake news during their studies. Previous research has shown that games are particularly effective for learning about fake news, but the group of pre-service teachers has not yet been investigated. The aim of this study is to address this gap by examining whether pre-service teachers can learn about fake news using the augmented reality escape game &lt;i&gt;Escape Fake&lt;/i&gt;. To investigate this question, a pre-/post-test design was conducted with 45 pre-service teachers (four males, mean age=22.59 years, standard deviation=1.80). The results show that after playing &lt;i&gt;Escape Fake&lt;/i&gt;, the pre-service teachers demonstrate significantly higher knowledge about fake news, are significantly more critical towards online information, and are significantly more confident in being able to recognize fake news in the future. However, playing the game did not promote the ability to discern real from false information. The paper discusses reasons for this finding and suggests ways to improve learning with the game. Implications and future research needs are discussed.",
  "reason": "Escape game em realidade aumentada com pré e pós-teste em 45 professores em formação."
 },
 {
  "id": "C92",
  "title": "ENHANCING MEDIA AND INFORMATION LITERACY THROUGH EXPERIENTIAL GAME-BASED LEARNING",
  "year": 2025,
  "venue": "Malaysian Journal of Learning and Instruction",
  "abstract": "Purpose – Media and Information Literacy (MIL) education plays a crucial role in combating misinformation and disinformation in the digital era. This study explores an innovative pedagogical approach by integrating Experiential Learning Theory (ELT) into non-digital game-based learning to bridge gaps in MIL knowledge and skills among Malaysian secondary and tertiary students, while also addressing the digital divide. Given that current MIL interventions often rely solely on self-assessment, this study emphasises the need for more objective assessment methods to measure actual learning outcomes. Methodology – A one-group pre-post-test mixed-methods research design was employed. A total of 95 participants from secondary and tertiary educational institutions in Malaysia engaged in an ELT-informed MIL board game intervention. The impact on MIL knowledge was assessed using a structured MIL knowledge test and a qualitative feedback survey. Findings – Results indicate that the intervention positively influenced MIL knowledge acquisition, as indicated by statistically significant improvements in post-test scores. Qualitative feedback further revealed enhanced understanding of MIL concepts, strengthened sense of responsible digital citizenship, and affirmation of the experiential game-based approach as an effective learning method. Significance – This study offers valuable insights into the application of ELT within non-digital game-based MIL education, particularly across diverse educational levels in Malaysia. It presents a scalable and cost-effective model for fostering critical thinking and ethical media engagement, offering practical recommendations for educators, community-based organisations, and policymakers in advancing MIL education nationwide.",
  "reason": "Jogo de tabuleiro de alfabetização midiática contra desinformação, com pré e pós-teste em 95 participantes."
 },
 {
  "id": "C67",
  "title": "Breaking the News: Taking the Roles of Influencer vs. Journalist in a LLM-Based Game for Raising Misinformation Awareness",
  "year": 2025,
  "venue": "Proceedings of the ACM on Human-Computer Interaction",
  "abstract": "Effectively mitigating online misinformation requires understanding of their mechanisms and learning of practical skills for identification and counteraction. Serious games may serve as tools for combating misinformation, teaching players to recognize common misinformation tactics, and improving their skills of discernment. However, current interventions are designed as single-player, choice-based games, which present players with limited predefined choices. Such restrictions reduce replayability and may lead to an overly simplistic understanding of misinformation and how to debunk them. This study seeks to empower people to understand opinion-influencing and misinformation-debunking processes. We created a Player vs. Player (PvP) game in which participants attempt to generate or debunk misinformation to convince the public opinion represented by LLM. Using a within-subjects mixed-methods study design (N=47), we found that this game significantly raised participants' media literacy and improved their ability to identify misinformation. Qualitative analyses revealed how participants' use of debunking and content creation strategies deepened their understanding of misinformation. This work shows the potential for illuminating contrasting viewpoints of social issues by LLM-based mechanics in PvP games.",
  "reason": "Jogo com modelo de linguagem para desinformação, avaliado em desenho intrassujeitos (N = 47). O periódico é Proceedings of the ACM on HCI, o que gera dúvida sobre ser anais."
 },
 {
  "id": "C69",
  "title": "Misinformation interventions decay rapidly without an immediate posttest",
  "year": 2024,
  "venue": "Journal of Applied Social Psychology",
  "abstract": "Abstract In recent years, many kinds of interventions have been developed that seek to reduce susceptibility to misinformation. In two preregistered longitudinal studies ( N 1 = 503, N 2 = 673), we leverage two previously validated “inoculation” interventions (a video and a game) to address two important questions in misinformation interventions research: (1) whether displaying additional stimuli (such as videos unrelated to misinformation) alongside an intervention interferes with its effectiveness, and (2) whether administering an immediate posttest (in the form of a social media post evaluation task after the intervention) plays a role in the longevity of the intervention. We find no evidence that other stimuli interfere with intervention efficacy, but strong evidence that immediate posttests strengthen the learnings from the intervention. In study 1, we find that 48 h after watching a video, participants who received an immediate posttest continued to be significantly better at discerning untrustworthy social media posts from neutral ones than the control group ( d = 0.416, p = .007), whereas participants who only received a posttest 48 h later showed no differences with a control ( d = 0.010, p = .854). In study 2, we observe highly similar results for a gamified intervention, and provide evidence for a causal mechanism: immediate posttests help strengthen people's memory of the lessons learned in the intervention. We argue that the active rehearsal and application of relevant information are therefore requirements for the longevity of learning‐based misinformation interventions, which has substantial implications for their scalability.",
  "reason": "O estudo 2 usa uma intervenção gamificada e testa a duração do efeito, N2 = 673. O estudo 1 usa vídeo."
 }
]