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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre os efeitos de manchetes caça-cliques (clickbait) sobre leitores e usuários de notícias. Restrições: apenas estudos empíricos com dados de leitores ou usuários (experimentos, questionários, medidas fisiológicas como EEG ou rastreamento ocular, ou dados de cliques e engajamento); exclua modelos computacionais de detecção ou classificação de clickbait, análises apenas linguísticas de manchetes sem dados de leitores e estudos com recorte político ou eleitoral. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CRITÉRIOS:
{
 "include": [
  "Artigo de periódico revisado por pares, publicado entre 2018 e 2025",
  "Estudo empírico com dados próprios de leitores ou usuários (experimento, survey, questionário, entrevistas, EEG, rastreamento ocular, cliques ou engajamento)",
  "Tema central: efeitos ou respostas de leitores/usuários a manchetes clickbait ou caça-cliques (atenção, credibilidade, confiança, intenção de clicar, compartilhamento, emoção, compreensão, engajamento)",
  "Contexto de notícias ou mídia noticiosa online/social",
  "Resumo disponível que permita identificar método e achado principal"
 ],
 "exclude": [
  "Modelos computacionais de detecção, classificação ou geração de clickbait (machine learning, NLP, deep learning)",
  "Análises apenas linguísticas ou de conteúdo de manchetes sem dados de leitores ou usuários",
  "Estudos com recorte político ou eleitoral (campanhas, eleições, polarização partidária, desinformação política)",
  "Revisões de literatura, revisões sistemáticas, meta-análises, ensaios teóricos ou conceituais, resenhas",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, teses e dissertações",
  "Publicações fora do período 2018–2025",
  "Estudos sem dados empíricos próprios (comentários, editoriais, análises de literatura)",
  "Clickbait fora do contexto de notícias (publicidade, marketing de produtos, YouTube de entretenimento) sem relação com leitores de notícias"
 ]
}

ARTIGOS INCLUÍDOS, COM O RESUMO BAIXADO POR CÓDIGO:
[
 {
  "id": "C13",
  "title": "Shocking secret you won’t believe! Emotional arousal in clickbait headlines",
  "year": 2019,
  "venue": "Online Information Review",
  "abstract": "Purpose Clickbait has become a popular strategy for attracting online users by enticing them to follow the link to a particular website to read further. The purpose of this paper is to fill a gap in the literature by providing empirical evidence of how clickbait headlines affect online users’ emotional and behavioral responses, specifically emotional arousal and intention to read news. In addition, it is an early attempt to examine pupillary dilation response as an indicator of emotional arousal in the online news context. Design/methodology/approach An experiment was conducted primarily to examine the levels of emotional arousal evoked by two treatment groups of online news headlines, news and clickbait, compared to a neutral control group. Emotional arousal was assessed using two approaches – pupillary dilation response recorded by an eye-tracking device and the Self-Assessment Manikin (SAM) – and the results were compared. The influence of emotional arousal on intention to read news was hypothesized and tested. Findings The level of emotional arousal evoked by the headlines varies. In general, clickbait headlines generate a higher level of emotional arousal than do the neutral headlines but a lower level than the news headlines. The results also indicate that the level of emotional arousal measured by pupillary dilation response and by SAM are somewhat consistent. Emotional arousal appears to be a significant predictor of intention to read news. Originality/value This study is an initial attempt to investigate how clickbait headlines influence online users’ perceptions and responses, which will be of interest to researchers and news media publishers. The current study also provides evidence for adopting pupillary dilation response, an unobtrusive measure of emotional response, as an alternative methodology for future studies that investigate emotional arousal related to textual information in the online news context.",
  "reason": "Experimento com rastreamento ocular (dilatação pupilar) e SAM sobre excitação emocional diante de manchetes clickbait."
 },
 {
  "id": "C03",
  "title": "Effects of Clickbait Headlines on User Responses: An Empirical Investigation",
  "year": 2021,
  "venue": "Journal of international technology and information management",
  "abstract": "This study investigates the influence of a conventional method of delivering news headlines, clickbait, on online users’ perceptions and responses. An experiment was conducted on two groups of news headlines—traditional news and clickbait—to provide empirical evidence of the effects of clickbait on online users. The findings suggest that clickbait headlines can evoke users’ arousal and curiosity. In addition, the results from structural equation modeling fill the gap in the literature by providing evidence of the factors influencing users’ intention to read and share online news. The results reveal that while the major determinant of users’ intention to read news stories is curiosity, perceived knowledge quality appears to be the main factor users consider when sharing online news stories.",
  "reason": "Experimento com usuários sobre efeitos de manchetes clickbait (curiosidade, excitação, intenção de ler e compartilhar)."
 },
 {
  "id": "C32",
  "title": "Exaggerated and Questioning Clickbait Headlines and Their Influence \t\t\t\t\ton Media Learning",
  "year": 2022,
  "venue": "Journal of Media Psychology",
  "abstract": "Abstract. Headlines that are incongruous with article content can negatively impact media learning outcomes. Clickbait headlines intentionally misrepresent news content, often in sensational ways to increase click-throughs and ad revenue. To evaluate the impact of clickbait headlines on media learning and article-related beliefs, we conducted two online experiments, each testing a 3 (headline-type: accurate, clickbait-question, clickbait-exaggerated) × 2 (exposure: headline-only, full article) factorial. In Study 1, an online sample of US adults ( N = 629) was randomly assigned to one of six news message conditions. Study 2 ( N = 1,674) was a replication study across three news contexts and testing a mediator to explain how exposure to a clickbait headline can influence learning. Key results suggest that reading the full article with an accurate headline resulted in the highest recognition and comprehension, and reading correcting information within an article is likely not enough to overcome the deleterious impact of a clickbait headline. Theoretical and practical recommendations are discussed.",
  "reason": "Dois experimentos online (N=629 e N=1.674) sobre clickbait e aprendizagem a partir da mídia."
 },
 {
  "id": "C106",
  "title": "Clickbait—Trust and Credibility of Digital News",
  "year": 2021,
  "venue": "IEEE Transactions on Technology and Society",
  "abstract": "Clickbait headlines are compelling and designed to lure readers to click on the linked article. To understand their impact on the credibility of news items, we designed and conducted an experiment on news articles from the Web is-Clickbait-17 dataset. The role of readers' age and epistemic curiosity (EC) on clickbait propensity was also studied. Two datasets of six articles each of news relevant to North America and India were selected and each article was assigned a clickbait and a nonclickbait headline based on a pretest for clickbait perception. 200 participants (100 each of English-speaking American and English-speaking Indian) were instructed to click and read through any two articles of their choice and fill a credibility questionnaire. Epistemic curiosity and demographic data were collected at the end of the experiment. Clickbait headlines significantly reduced the credibility of news items. A correlation between age and propensity for clickbait was observed. No correlation was observed between diversive EC and clickbait propensity, while a weakly negative correlation was observed between specific EC and clickbait propensity. We hope that our findings may lead to a better end-user experience in terms of access to credible information for news readers, bereft of clickbait.",
  "reason": "Experimento com 200 participantes mostrando que clickbait reduz a credibilidade de notícias."
 },
 {
  "id": "C107",
  "title": "Aggregation, Clickbait and Their Effect on Perceptions of Journalistic Credibility and Quality",
  "year": 2019,
  "venue": "Journalism Practice",
  "abstract": "Many journalists and industry observers lament that aggregating news underneath sensational headlines will erode credibility and turn off readers. While some scholarly work has studied journalists’ perspectives of this practice, little has been done to understand what audiences think of aggregation and clickbait. This study uses published original and aggregated news articles as stimuli in two online experiments to test readers’ perceptions of news aggregation and clickbait. Aggregation itself has little effect on perceptions of credibility and quality; instead, writing proficiency is more closely linked to these perceptions. Results also suggest clickbait headlines may lower perceptions of credibility and quality.",
  "reason": "Dois experimentos online sobre clickbait, credibilidade e qualidade percebidas."
 },
 {
  "id": "C110",
  "title": "The curiosity effect: Information seeking in the contemporary news environment",
  "year": 2019,
  "venue": "New Media & Society",
  "abstract": "This research investigates how digital news headlines influence contemporary news information seeking. In two studies (a lab experiment and a field test), we examine how the presentation of news information—traditional, summary news headlines or clickbait, curiosity news headlines—influences the attitudinal and behavioral components of news seeking. Study 1 models the news-seeking process, finding that summary headlines heighten perceptions of headline information adequacy, which increase expectations that an article will provide clear information, which in turn increase anticipated audience engagement with news compared to some curiosity headlines. Study 2 determines that individuals’ selection behavior on nine local newspaper websites also favors summary headlines. The findings encourage researchers to employ information-seeking mechanisms in understanding news selection decisions.",
  "reason": "Experimento de laboratório e teste de campo sobre busca de notícias com manchetes de curiosidade (clickbait)."
 },
 {
  "id": "C21",
  "title": "Clickbait-style headlines and journalism credibility in Sub-Saharan Africa: Exploring audience perceptions",
  "year": 2021,
  "venue": "Journal of Media and Communication Studies",
  "abstract": "In the proliferated age of technologies, the field of journalism has been faced with several challenges that have inevitably pushed journalism practice to unpreceded heights. Overtly, journalists have resorted to various strategies to compete with various media platforms such as social media and other citizen journalistic strategies. Journalists have also resorted to the use of advertising/strategic communication methods to spice up their news stories and attract a large following. Particularly, journalists now use clickbait styles to draw more readership of their own stories. While this has been perceived as a pitfall for journalism, others have argued in favor of these strategies suggesting that they have no effect on the credibility of the media and journalism at large. This experimental study, therefore, set out to understand how the audience perceives clickbait-style headlines in relations to media credibility. Particularly, the study examined whether the Zambian and Tanzanian online news consumers observe the same distinction in the credibility of news content alleged to exist between clickbait and traditional news reporting, and whether perceptions of clickbait headlines lead to lower credibility for news articles. The findings suggest strong statistical evidence that clickbait headlines pose negatives effects on the perceptions of journalistic credibility in Zambia and Tanzania. Key words: Journalism credibility, clickbait, news wire-copying, online news consumers, Zambia, Tanzania.",
  "reason": "Experimento com consumidores de notícias online na Zâmbia e na Tanzânia sobre credibilidade."
 },
 {
  "id": "C109",
  "title": "Attention Grabbing through Forward Reference: An ERP Study on Clickbait and Top News Stories",
  "year": 2022,
  "venue": "International Journal of Human-Computer Interaction",
  "abstract": "Social media tends to use “catchy” headlines to intentionally get people to click news. However, clickbait headlines can erode readers’ trust and devalue news. To combat clickbait, it is necessary to understand how clickbait headlines influence readers’ clicking behavior and attention allocation. In this study, the researchers first collected headlines of news stories that had different amount and duration of media coverage, then identified whether these headlines include forward-reference strategies, and conducted an EEG experiment based on N2b and P3a. The results showed that the clickbait headlines with a forward-reference device attracted more attention resources and induced the involuntary attention allocation more quickly, compared with those without a forward-reference device. Unexpectedly, whether the news stories were top news stories or non-top news stories didn’t significantly influence the attention allocation.",
  "reason": "Experimento de EEG (ERP) sobre atenção a manchetes clickbait."
 },
 {
  "id": "C06",
  "title": "Decoding Clickbait: The Impact of Clickbait Types and Structures on Cognitive and Emotional Responses in Online Interactions",
  "year": 2024,
  "venue": "Cyberpsychology Behavior and Social Networking",
  "abstract": "This study delves into the influence of clickbait types (hyperbole, insinuation, visual rhetoric, and puzzle) and structures (emotion-label and emotion-laden words) on user cognitive and emotional responses in an online environment. Using electroencephalography with 32 internet-experienced participants, we analyzed how these different clickbait configurations affect engagement and processing. Our findings highlight that clickbait types such as hyperbole and visual rhetoric swiftly capture attention and enhance emotional engagement, whereas insinuative and puzzling clickbait demand more cognitive effort and deeper processing. In addition, the structure of emotional words significantly influences user responses; emotion-laden words facilitate quicker cognitive processing and enhance emotional reactions, particularly in contexts involving negative emotions. These insights offer valuable implications for content creators and marketers in strategizing ethical clickbait usage, aiming to balance user engagement with information integrity. This research contributes to a nuanced understanding of the interplay between content presentation and user perception, providing a foundation for future explorations into ethical digital content practices.",
  "reason": "Estudo de EEG com 32 participantes sobre respostas cognitivas e emocionais a clickbait; o resumo não cita notícias de forma explícita, é um ponto de dúvida."
 },
 {
  "id": "C40",
  "title": "“This Will Blow Your Mind”: examining the urge to click clickbaits",
  "year": 2020,
  "venue": "Aslib Journal of Information Management",
  "abstract": "Purpose Integrating the uses and gratifications (U&G) theory, the notion of information richness and personal epistemology framework, the purpose of this research is to propose and empirically validate a framework which specifies Internet users' urge to click clickbaits. Design/methodology/approach The hypotheses in the proposed framework were tested using a between-participants experimental design (N = 204) that manipulated information richness (text-only vs. thumbnail clickbaits). Findings Curiosity, perceived enjoyment and surveillance were significant predictors of the urge to click. In terms of information richness, the urge to click was higher for thumbnail vis-à-vis text-only clickbaits. IEB (IEB) moderated the relation between the gratification of passing time and the urge to click. Originality/value This paper represents one of the earliest attempts to investigate Internet users' urge to click clickbaits. Apart from extending the boundary conditions of the U&G theory, it integrates two other theoretical lenses, namely, the notion of information richness and personal epistemology framework, to develop and empirically validate a theoretical framework.",
  "reason": "Experimento (N=204) sobre a vontade de clicar em clickbaits; o resumo não cita notícias explicitamente, é um ponto de dúvida."
 },
 {
  "id": "C02",
  "title": "AI vs. Human-Authored Headlines: Evaluating the Effectiveness, Trust, and Linguistic Features of ChatGPT-Generated Clickbait and Informative Headlines in Digital News",
  "year": 2025,
  "venue": "Information",
  "abstract": "This study explores possible applications of AI technology in online journalism, given the predictions that speed and adaptation to the new medium will increase the penetration of automation in the production business. The literature shows that while the human supervision of journalistic workflow is still considered vital, the journalistic workflow is changing in nature, with the writing of micro-content being entrusted to ChatGPT-3.5 among the most visible features. This research assesses readers’ reactions to different headline styles as tested on a sample of 624 students from Timisoara, Romania, asked to evaluate the qualities of a mix of human-written vs. AI-generated headlines. The results show that AI-generated, informative headlines were perceived by more than half of the respondents as the most trustworthy and representative of the media content. Clickbait headlines, regardless of their source, were considered misleading and rated as manipulative (44.7%). In addition, 54.5% of respondents reported a decrease in trust regarding publications that frequently use clickbait techniques. A linguistic analysis was conducted to grasp the qualities of the headlines that triggered the registered responses. This study provides insights into the potential of AI-enabled tools to reshape headline writing practices in digital journalism.",
  "reason": "Survey com 624 estudantes sobre confiança e percepção de manchetes clickbait em notícias digitais."
 },
 {
  "id": "C42",
  "title": "Are ChatGPT-Generated Headlines Better Attention Grabbers than Human-Authored Ones? An Assessment of Salient Features Driving Engagement with Online Media",
  "year": 2024,
  "venue": "Journalism and Media",
  "abstract": "This study focuses on the case of news headlines in current online journalism, looking into the current possibilities opened by ChatGPT to generate such texts in an attention-grabbing manner. To assess the reaction of online readers to headlines (clickbait or click-worthy), an online survey was applied, involving Romanian students. A total of 100 original human-authored articles with clickbait headlines were extracted from a relevant Romanian database. ChatGPT was used to generate alternative headlines (one clickbait and one informative) based on the original texts. The resulting corpus of 100 headline triplets was offered to students for evaluation. More than 70% of the 600 participants in the survey preferred AI-generated headlines over the human-authored ones, indicating their experiences and behaviors in media consumption. The preferred headlines were further analyzed along lexical and grammatical characteristics, and stylistically, to pinpoint the features sparking readers’ curiosity and engagement. While on a cognitive level the investigated audience rejected clickbait headlines as being deceitful and frustrating, in practice less than 34% favored neutral and objective headlines. Also, the linguistic analysis provided insights into the mechanics of reader engagement and the effectiveness of various headline strategies. The results are useful to anticipate the adoption of AI as a creative partner in Romanian media practice.",
  "reason": "Survey com 600 participantes sobre reação a manchetes clickbait e informativas."
 },
 {
  "id": "C09",
  "title": "The Effect of Clickbait Headlines on Tribunnews.Com Online News Articles on the Reading Interest of Generation Z at FKI UMS",
  "year": 2025,
  "venue": "Riwayat Educational Journal of History and Humanities",
  "abstract": "development of digital technology has brought about significant changes in information consumption patterns, particularly among Generation Z. One phenomenon that has emerged is the use of clickbait headlines on online news portals as a strategy to capture readers' attention. This study aims to analyze the effect of clickbait headlines on Tribunnews.com on the reading interest of Generation Z students at the Faculty of Communication and Informatics, Universitas Muhammadiyah Surakarta. This study employs a quantitative approach using a survey method through a questionnaire distributed to 113 respondents. The sampling technique used is purposive sampling. The results indicate that the use of clickbait headlines has a significant influence on reading interest. The effects are not only an increase in curiosity but also lead to boredom or disappointment when the news content does not match the expectations set by the headline. These findings reinforce the Uses and Effects Theory, which states that media directly impacts readers' behavior, both in terms of increasing curiosity and causing boredom when the news content does not meet expectations.",
  "reason": "Survey com 113 respondentes sobre o efeito de manchetes clickbait no interesse de leitura."
 },
 {
  "id": "C11",
  "title": "Click me…! The influence of clickbait on user engagement in social media and the role of digital nudging",
  "year": 2022,
  "venue": "PLoS ONE",
  "abstract": "Clickbait to make people click on a linked article is commonly used on social media. We analyze the impact of clickbait on user interaction on Facebook in the form of liking, sharing and commenting. For this, we use a data set of more than 4,400 Facebook posts from 10 different news sources to analyze how clickbait in post headlines and in post text influences user engagement. The results of our study revealed that certain features (e.g., unusual punctuation and common clickbait phrases) increase user interaction, whereas others decrease engagement with Facebook posts. We further use our results to discuss the potential role of digital nudging in the context of clickbait. Our results contribute to understanding and making use of the effect of different framings in social media.",
  "reason": "Dados de engajamento (curtir, compartilhar, comentar) em mais de 4.400 posts de fontes de notícias no Facebook."
 },
 {
  "id": "C24",
  "title": "Analyzing Sensationalism in News on Twitter ( X ): Clickbait Journalism by Legacy vs. Online-Native Outlets and the Consequences for User Engagement",
  "year": 2024,
  "venue": "Digital Journalism",
  "abstract": "News consumption patterns have evolved as people increasingly get news through social media. A by-product of this change has been the rise of “clickbaits”—a form of journalism that utilizes sensationalist techniques to lure readers into clicking on links. Although clickbaits have become common, not much is known about the use of this journalistic practice. This study empirically investigates whether online-native news outlets utilize more sensational features than legacy news outlets to promote their news stories on Twitter (now X). The impact of sensationalism on subsequent user engagement metrics is also tested. First, a manual content analysis of 1,440 tweets by news media organizations was conducted, identifying sensationalism through ten features. Second, an automated content analysis was conducted on a dataset of 25,600 tweets, replicating the manual coding process. The results confirm that online-native outlets (Huffington Post, BuzzFeed) utilized more sensationalism than online legacy outlets (USA Today, L.A. Times). Furthermore, a positive relationship was found between the number of sensationalist features employed and the favorite count, confirming the effectiveness of clickbaits. The automated content analysis by-and-large corroborated the findings of the manual annotation, and additionally revealed a positive effect of sensationalism on the number of retweets.",
  "reason": "Análise de engajamento (favoritos e retuítes) em relação a recursos de sensacionalismo/clickbait em tuítes de veículos de notícias."
 },
 {
  "id": "C37",
  "title": "A STUDY OF CLICKBAIT TITLES:",
  "year": 2021,
  "venue": "At-Tanzir Jurnal Ilmiah Prodi Komunikasi Penyiaran Islam",
  "abstract": "Perkembangan arus globalisasi membawa banyak sekali perubahan dalam berbagai aspek kehidupan, salah satunya adalah media informasi. Perubahan ini membuat media informasi terus berevolusi dalam memengaruhi lanskap media dengan menjaring media online. Seringkali judul-judul artikel yang tampil di media online terlalu berlebihan bahkan tidak sesuai dengan isi dari artikel tersebut. Fenomena ini sering disebut umpan klik. Penelitian ini bertujuan untuk mengkaji lebih lanjut judul-judul artikel yang mengandung umpan klik menurut perspektif pengguna media online. Penelitian dilakukan dengan metode kuantitatif dengan teknik pengumpulan data menggunakan kuesioner atau angket. Sampel pada penelitian kali ini adalah pengguna media online. Hasil penelitian yang dilakukan menunjukkan lebih dari setengah pengguna media online tidak asing dengan kata umpan klik. Akan tetapi, masih banyak pengguna media online yang belum memahami berita umpan klik dalam konteks yang sebenarnya. Tidak hanya itu, meskipun umpan klik dianggap manipulasi atau jebakan, masyarakat terutama pengguna media online justru sadar bahwa mereka membaca artikel atau berita yang berjudul umpan klik untuk memenuhi rasa penasaran dari sensasi yang ditimbulkan oleh judul umpan klik tersebut.",
  "reason": "Questionário quantitativo com usuários de mídia online sobre clickbait."
 },
 {
  "id": "C45",
  "title": "Critical literacy: prevents negative impact of clickbait news on news agency website",
  "year": 2022,
  "venue": "Library Hi Tech News",
  "abstract": "Purpose This study aims to describe the critical literacy of online newsreaders on the viva.co.id website in dealing with clickbait news. Critical literacy is oriented to the critical power of online newsreaders by analyzing, evaluating and reflecting on the relationship of online newsreaders, texts and social and political contexts. This research will focus on the type of clickbait exaggeration or news headlines that use exaggeration. Design/methodology/approach This study uses a quantitative method with a descriptive approach. The purpose of quantitative research is to provide information on a situation by using scientific procedures to answer a question in an actual way (Sugiyono, 2010). Scientific observation is carried out carefully to obtain accurate results on a phenomenon. This study presents an overview of the situation or a phenomenon regarding the critical literacy of online newsreaders on the viva.co.id website in dealing with clickbait titles in Surabaya. The population in this study were all online newsreaders entitled clickbait on the viva.co.id website, where the number of online newsreaders on the viva.co.id website was not known. Sampling in this study used the Lemeshow formula (Lemeshow, 1997, as cited in Priyambodo, 2019). This formula determines the number of samples if the population is not known. Based on the calculation using the Lemeshow formula, it can be seen that the minimum sample size required is 96 respondents who are rounded up to 100 respondents with a 95% confidence level. Findings Based on the findings of the data recapitulation of the overall dimensions of critical literacy, this study shows that newsreaders entitled clickbait on the website viva.co.id have critical literacy skills that fall into the high category with an overall average of 4.07. This finding shows positive results because critical literacy skills are skills needed by newsreaders entitled clickbait on the website viva.co.id. Currently, online news is very much in number, and it may be that the news is not by the existing facts; therefore, this ability is considered very important because, with this ability, the reader can find out the ideology or interests that affect a news publication (Priyatni, 2010). Research limitations/implications This research only uses an online news provider, namely, viva.co.id, it is an Indonesia-based online news provider that covers all news subjects. Practical implications This study will give understanding about the use of critical literacy to prevent negative impact on clickbait and is very useful for all online newsreaders, information practitioners and scientists. Originality/value The use of critical literacy to assess online news is rarely studied in Indonesia, especially when dealing with clickbait news that can harm or bring disadvantages for readers. So, this study is very important to help readers to prevent clickbait news.",
  "reason": "Survey com cerca de 100 leitores sobre letramento crítico diante de notícias clickbait."
 },
 {
  "id": "C20",
  "title": "CLICKBAIT SEBAGAI STRATEGI FRAMING BERITA DALAM MEDIA DARING TRIBUNNEWS.COM CLICKBAIT AS A NEWS FRAMING STRATEGY IN THE ONLINE MEDIA TRIBUNNEWS.COM",
  "year": 2025,
  "venue": "KAGANGA KOMUNIKA: Journal of Communication Science",
  "abstract": "Penelitian ini bertujuan untuk memahami bagaimana penggunaan judul clickbait dalam pemberitaan Tribunnews.com memengaruhi tingkat kepercayaan mahasiswa Ilmu Komunikasi UNISKA MAB terhadap informasi yang disajikan. Fenomena clickbait yang kian marak di media daring dinilai efektif dalam menarik perhatian pembaca, namun menimbulkan kekhawatiran terkait akurasi informasi, etika jurnalistik, dan kepercayaan publik. Penelitian ini menggunakan pendekatan kualitatif dengan metode studi kasus, melibatkan delapan mahasiswa Ilmu Komunikasi sebagai informan yang dipilih secara purposif. Teknik pengumpulan data meliputi observasi, dokumentasi, dan wawancara mendalam. Hasil penelitian menunjukkan bahwa sebagian besar mahasiswa menyadari keberadaan clickbait dalam berita Tribunnews.com, terutama pada rubrik hiburan dan gaya hidup. Mahasiswa menilai bahwa meskipun judul berita mampu menarik perhatian, konten yang tidak sesuai dengan judul dapat mengurangi kredibilitas dan menimbulkan rasa tidak percaya. Terdapat perbedaan persepsi antara mahasiswa yang sering terpapar clickbait dan yang tidak, di mana kelompok pertama cenderung bersikap lebih skeptis namun permisif terhadap fenomena tersebut, sementara kelompok kedua lebih mengedepankan keakuratan dan substansi informasi. Penelitian ini merekomendasikan peningkatan literasi media bagi mahasiswa serta dorongan bagi media daring untuk menjaga keseimbangan antara daya tarik judul dan kualitas isi berita. Kata Kunci: Clickbait, Kepercayaan Media, Tribunnews.Com, Media Daring",
  "reason": "Estudo qualitativo com entrevistas a 8 estudantes sobre confiança diante de manchetes clickbait."
 },
 {
  "id": "C69",
  "title": "The Impact of Clickbait News on Online Media Audiences from the Perspective of Islamic Communication: A Case Study of PALTV.disway.id Palembang",
  "year": 2025,
  "venue": "AJIS Academic Journal of Islamic Studies",
  "abstract": "The phenomenon of clickbait news dissemination in online media has become a serious concern due to its potential influence on readers’ mindsets and behavior, particularly within Muslim communities. This study aims to analyze the impact of clickbait news on readers of PALTV.disway.id in Palembang City from the perspective of Islamic communication. The research employs a qualitative method with a descriptive approach, utilizing observation, in-depth interviews with active readers, journalists, and religious figures, as well as documentation analysis. The findings indicate that clickbait news frequently leads to information misunderstanding and a decline in the quality of readers’ Islamic understanding, especially when headlines are not aligned with the content. From the perspective of Islamic communication, such practices contradict the principles of ṣidq (truthfulness), tablīgh (transparency), and amānah (trustworthiness) in information dissemination. Another finding reveals an increased level of skepticism toward media outlets that present Islamic issues, driven by the frequent use of provocative headlines unsupported by adequate content. This study highlights the urgency of integrity in Islamic journalism and the importance of media literacy within society. The integration of digital media analysis with Islamic communication principles constitutes the originality of this research. The results are expected to provide practical contributions for media practitioners, government institutions, and da‘wah organizations in formulating more ethical communication strategies, as well as academic contributions to the development of Islamic communication studies in the digital era.",
  "reason": "Entrevistas com leitores sobre o impacto de notícias clickbait."
 },
 {
  "id": "C64",
  "title": "You’re Being Kinda Pushy: Exploring How News Outlets Frame Push Notifications as Credible Clickbait to Engage with Their Audiences",
  "year": 2025,
  "venue": "Journalism and Media",
  "abstract": "Push notifications are a digital strategy for outlets to provide news and a convenient way for audiences to absorb information. Past research shows the effectiveness of push notifications and how they are framed, but few studies have explored their relationship with clickbait. However, clickbait often has a negative connotation. Through an exploratory mixed methods study involving textual analysis of push notifications (n = 639) sent by three credible mainstream media outlets, namely The Associated Press, The New York Times, and The Wall Street Journal, and a survey of readers’ (n = 368) perception of push notifications and clickbait, this research explores how credible news outlets directly engage with their respective audiences by framing push notifications in the form of clickbait. This study builds on framing theory by proposing the concept of credible clickbait and illustrating how push notifications shape readers’ immediate perceptions of content being shared with them by news outlets they subscribe to. This research also aims to be a resource for journalists to increase audience interaction and foster sustained attention with stories.",
  "reason": "Método misto com survey de 368 leitores sobre a percepção de notificações push e clickbait."
 },
 {
  "id": "C41",
  "title": "Sensational Headlines, Engagement, and Credibility in Nepal’s Online News",
  "year": 2025,
  "venue": "Nepalese Journal of Development and Rural Studies",
  "abstract": "This study examines whether sensational headlines in Nepal’s online news ecosystem generate short-term audience engagement while weakening perceived credibility. A convergent cross-methods design was used. The quantitative component comprised a content analysis of 300 Facebook-posted headlines from three prominent Nepali news portals - OnlineKhabar, The Kathmandu Post, and The Himalayan Times - collected between June 15 and July 15, 2024. Headlines were coded as sensational or non-sensational using indicators of emotional language, hyperbole, provocative framing, and curiosity-gap construction. Visible Facebook engagement indicators - likes, shares, and comments - were descriptively compared across headline types. The audience component consisted of a purposive survey of 81 Nepali online news consumers on news-use habits, trust perceptions, and coping practices. Sensational headlines constituted 43% of the sampled posts, with outlet-level variation from 36% to 52%. Sensational headlines received higher mean engagement than non-sensational headlines, especially for comments; however, survey responses indicated credibility costs, including skepticism, cross-checking, and avoidance of repeatedly sensational outlets. The findings support attention-economy and platform-diffusion arguments that emotionally salient headlines can attract attention in algorithmic feeds, but they also show that repeated sensationalism may impose a long-term trust penalty. For Nepali newsrooms, sustainable digital journalism requires balancing headline visibility with accuracy, transparency, and audience trust.",
  "reason": "Engajamento no Facebook e survey com 81 leitores sobre manchetes sensacionalistas e credibilidade."
 },
 {
  "id": "C18",
  "title": "PHOTOGRAPHY AND CLICKBAIT HEADLINES: ONLINE MEDIA TOOLS IN THE PROCESS OF READERS MANIPULATION",
  "year": 2022,
  "venue": "SPORTS, MEDIA AND BUSINESS",
  "abstract": "Online media no longer play only an informative role. One of the goals in the fight for profit is to be visited as much as possible. However, the rush to publish the news before competitors can also manipulate readers. Interestingly, photography is a powerful media tool. As a reminder, one of the first forms of photo manipulation was during the Crimean War. Photographer Roger Fenton was assigned the task of depicting the conflict more beautifully, confirming Queen Victoria's manipulation and inspiring the nation to fight. For online media in the 21st century, it is not enough to suggest content with a photo, which is why clickbait headlines play a role in the whole process. In this paper, I conducted research with 200 respondents to prove the thesis that clickbait headlines and photography are tools in the manipulation process, even using sports news examples. Participants indicated their agreement or disagreement with the statements using a Likert scale. They were also manipulated by the photos and clickbait headlines, according to the results.",
  "reason": "Survey com 200 respondentes sobre manipulação por manchetes clickbait e fotos em notícias esportivas."
 },
 {
  "id": "C23",
  "title": "Headline Format Influences Evaluation of, but Not Engagement with, Environmental News",
  "year": 2020,
  "venue": "Journalism Practice",
  "abstract": "Sparked by a collaboration between academic researchers and science media professionals, this study sought to test three commonly used headline formats that vary based on whether (and, if so, how) important information is left out of a headline to encourage participants to read the corresponding article; these formats are traditionally-formatted headlines, forward-referencing headlines, and question-based headlines. Although headline format did not influence story selection or engagement, it did influence participants evaluations of both the headline's and the story's credibility (question-based headlines were viewed as the least credible). Moreover, individuals’ science curiosity and political views predicted their engagement with environmental stories as well as their views about the credibility of the headline and story. Thus, headline formats appear to play a significant role in audience's perceptions of online news stories, and science news professionals ought to consider the effects different formats have on readers.",
  "reason": "Experimento com formatos de manchete (referência adiante e pergunta) sobre credibilidade e engajamento em notícias ambientais; a ligação com clickbait é indireta."
 }
]