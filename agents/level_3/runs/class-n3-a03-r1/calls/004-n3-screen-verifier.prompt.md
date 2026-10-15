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
Encontre 25 artigos científicos revisados por pares, publicados em periódicos entre 2018 e 2025, sobre desinformação e educação midiática (ou competência em informação) em escolas e universidades brasileiras. Restrições: estudos empíricos feitos no Brasil com estudantes, professores, aulas, currículos ou livros didáticos (questionários, grupos focais, intervenções, relatos de experiência com coleta de dados ou análise documental); estudos comparativos internacionais valem se incluírem amostra brasileira; exclua estudos centrados em COVID-19, vacinas, eleições ou política partidária e estudos com públicos fora do ensino formal. Valem apenas artigos de periódico que relatem estudo empírico com dados próprios; não use revisões de literatura, meta-análises, ensaios teóricos, preprints, trabalhos de anais de congresso, capítulos de livro, teses ou resenhas. Para cada artigo, informe: DOI; título; autores; ano de publicação; periódico; tipo de estudo e método; tamanho da amostra exatamente como aparece no resumo (ou "não informado no resumo"); achado principal, em uma frase; e um trecho literal do resumo, entre aspas, que sustente o achado principal.

CRITÉRIOS:
{
 "include": [
  "Artigo de periódico revisado por pares publicado entre 2018 e 2025",
  "Estudo empírico com dados próprios (questionário, entrevista, grupo focal, intervenção, experimento, relato de experiência com coleta de dados, análise documental de currículos ou livros didáticos)",
  "Tema central: desinformação/fake news/notícias falsas e educação midiática, letramento midiático ou competência em informação",
  "Realizado no Brasil, com estudantes, professores, aulas, currículos ou livros didáticos em escolas ou universidades (ensino formal)",
  "Estudos comparativos internacionais somente se incluírem amostra brasileira",
  "Resumo disponível e permite identificar método e achado principal"
 ],
 "exclude": [
  "Revisões de literatura, revisões sistemáticas, meta-análises",
  "Ensaios teóricos ou artigos puramente conceituais sem dados empíricos",
  "Preprints, trabalhos de anais de congresso, capítulos de livro, livros, teses, dissertações, resenhas",
  "Estudos centrados em COVID-19, vacinas, eleições ou política partidária",
  "Públicos fora do ensino formal (população geral, idosos, jornalistas, redes sociais abertas sem contexto escolar)",
  "Estudos sem amostra brasileira ou realizados fora do Brasil",
  "Publicações fora do período 2018–2025",
  "Estudos sobre desinformação sem componente educacional (ex.: detecção automática, análise de redes)"
 ]
}

ARTIGOS INCLUÍDOS, COM O RESUMO BAIXADO POR CÓDIGO:
[
 {
  "id": "C28",
  "title": "A competência crítica em informação na web para o combate à fake news",
  "year": 2025,
  "venue": "Biblionline",
  "abstract": "O artigo relata e analisa a aplicação do Projeto de Ação na Escola (PAE), desenvolvido no âmbito do curso de especialização em Tecnologias da Informação e Comunicação na Educação da Universidade Federal do Rio Grande. O objetivo central da iniciativa foi fomentar o desenvolvimento da competência crítica em informação na web, com base em uma metodologia construtivista apoiada por recursos tecnológicos. A atividade foi realizada com 20 estudantes do ensino médio, na biblioteca de uma escola pública no interior do RS, articulando plataformas digitais como Google Classroom, Kahoot e Canva, além de dispositivos como computadores e smartphones. A proposta pedagógica, organizada na forma de Unidade de Aprendizagem, possibilitou a construção dialógica do conhecimento e o estímulo à análise crítica das informações veiculadas na internet. Os dados obtidos, por meio de questionários, atividades gamificadas e observações, revelaram dificuldades iniciais dos alunos em distinguir informações verídicas de fake news. Contudo, após a aplicação do projeto, observou-se significativo aprimoramento na capacidade de checagem e avaliação crítica de conteúdos, com 80% dos participantes declarando ter desenvolvido sua competência crítica em informação. Os resultados indicam que a metodologia adotada contribuiu para o engajamento, a autonomia e o protagonismo dos estudantes no processo de aprendizagem. As conclusões reforçam o papel das bibliotecas como espaços formativos e a importância de metodologias ativas aliadas às tecnologias digitais para o enfrentamento da desinformação e a promoção de uma cultura informacional crítica.",
  "reason": "Projeto com 20 estudantes do ensino médio de escola pública do RS sobre competência crítica em informação e fake news, com questionários e atividades."
 },
 {
  "id": "C20",
  "title": "Todos contra a desinformação",
  "year": 2025,
  "venue": "INTERIN",
  "abstract": "O artigo aborda uma intervenção pedagógica (Damiani et al., 2013) focada na educação midiática para o Ensino Médio, realizada em uma escola pública no Espírito Santo, Brasil. O contexto está relacionado à crescente preocupação com a desinformação, um fenômeno amplificado pela hiperconexão digital e que desafia a capacidade dos jovens de distinguir fatos de opiniões, ou mesmo de identificar informações falsas. O objetivo principal foi formar leitores críticos e conscientes. O plano de ação da intervenção pedagógica incluiu metodologias ativas como aprendizagem em equipes e investigação por meio de estudo dirigido, explorando textos diversos e recursos audiovisuais. Durante a intervenção, os alunos participaram de debates e estudo de caso. Os resultados mostraram progresso na compreensão sobre desinformação e habilidades de interpretação textual, embora alguns desafios, como engajamento desigual, tenham sido observados. A intervenção destacou a importância de estratégias inovadoras no ensino de Língua Portuguesa, conectando teoria e prática à realidade social dos alunos.",
  "reason": "Intervenção pedagógica em educação midiática e desinformação com alunos do Ensino Médio de escola pública brasileira."
 },
 {
  "id": "C120",
  "title": "Real ou Fake: desenvolvimento e aplicação de um jogo de cartas para o combate à desinformação no interior do Pará",
  "year": 2023,
  "venue": "Revista Contracampo",
  "abstract": "Este artigo tem como objetivo refletir sobre o uso de materiais didáticos no combate à desinformação para o ensino básico como apoio a ações de educação e letramento midiático. A dinâmica parte de uma pesquisa-ação desenvolvida na Escola de Ensino Médio Dionísio Bentes de Carvalho, em Rondon do Pará/PA, na Amazônia Oriental, local considerado como deserto de notícias devido à escassez de informação jornalística local. A partir de uma pesquisa sobre o consumo de mídia por parte dos jovens do terceiro ano, foi produzido um jogo de cartas chamado Real ou Fake, posteriormente aplicado a esses estudantes. Os resultados evidenciam que o jogo pode ser uma oportunidade de se trabalhar em sala de aula conteúdos atuais e de interesse dos estudantes para que desenvolvam competência crítica em relação à mídia.",
  "reason": "Pesquisa-ação com estudantes do 3º ano do ensino médio no Pará, com jogo de cartas contra a desinformação e levantamento do consumo de mídia."
 },
 {
  "id": "C39",
  "title": "Media and information literacy strategies: A joint reflection with teenagers in Brazilian public school",
  "year": 2025,
  "venue": "Journal of Media Literacy Education",
  "abstract": "This article presents the findings from a Media and Information Literacy (MIL) project developed by journalism professors from University of Brasilia and conducted on elementary school students in Brazil. It examines teenagers' information practices and discusses the challenges of introducing MIL practices in the current state of information disorder. This study involves a survey and participant observation from a workshop conducted with these students in October 2021. The major strategies used to promote MIL practices and critical thinking among the students were: a) encouraging them to reflect on their own information practices; b) drawing on their experiences to help them reflect on the quality of the information; and c) de-normalizing disinformation and the problems it causes by stressing the consequences they have on society. This study emphasizes the importance of more organic MIL actions that could help avoid any prejudiced or condescending interpretations of teenagers’ information practices.",
  "reason": "Survey e observação participante em oficina de alfabetização midiática com adolescentes de escola pública brasileira em um contexto de desinformação."
 },
 {
  "id": "C43",
  "title": "The perception of misinformation by young students from a Brazilian sociocultural context: reflections and clues for media education",
  "year": 2024,
  "venue": "Observatorio (OBS*)",
  "abstract": "Based on a doctoral study developed in the Brazilian sociocultural context, the article reflects on the perception of misinformation among young students from public and private schools. In a society permeated by the digital world in the broader context of socio-materiality, the complexity of the terms Misinformation, Fake News, and Post-truth shows the difficulty of understanding true and false nowadays. In the capitalism of data, algorithms, control, and vigilance, misinformation is an increasingly discussed theme in digital culture due to the problems created in the political, economic, social, cultural, and political spheres. The implications of this phenomenon reverberate throughout the educational ecosystem, the teaching-learning interactions and relations in the school, and other informal and non-formal educational spaces. Grounded on the dialogue between cultural studies, media-education, and youth cultures, we seek to identify young students' perceptions of misinformation to create a formative path in the media-education perspective. The qualitative and exploratory research involved an empirical dimension conducted with young students from 14 to 21 years old in Curitiba and Colombo in Paraná, Brazil. We traced the group's profile through the European Framework for Digital competencies during workshops on media education, aiming to identify and reflect on how young students receive, understand, analyze, check, and share information. The workshop analyses suggested clues to build media competencies in the youth culture contexts and how schools can/should develop a work in the perspective of media education to build a better understanding of oneself, the other, and the world, producing and sharing messages and information with more responsibility in the perspectives of citizenship and belonging.",
  "reason": "Pesquisa qualitativa com oficinas de educação midiática com jovens estudantes de escolas públicas e privadas no Paraná sobre percepção da desinformação."
 },
 {
  "id": "C21",
  "title": "Literacias E Educação Midiática",
  "year": 2024,
  "venue": "Revista Latinoamericana de Ciencias de la Comunicación",
  "abstract": "Analisou-se a habilidade de professores e alunos do Ensino Médio, de escolas públicas e privadas no Brasil, em identificar fake news. Observou-se também o possível impacto que conteúdos educativos relacionados à desinformação podem oferecer aos respondetes ao analisar informações potencialmente falsas. Os resultados apontam a insuficiência de apenas explicar o que é informação falsa e como verificar, e sugere a necessidade de elaboração de planos a longo prazo que estimulem o pensamento crítico sobre o papel da mídia e do consumo de informações.",
  "reason": "Estudo com professores e alunos do Ensino Médio de escolas brasileiras sobre identificação de fake news e conteúdo educativo."
 },
 {
  "id": "C76",
  "title": "DESINFORMAÇÃO E LITERACIA MIDIÁTICA DISINFORMATION AND MEDIA LITERACY DESINFORMACIÓN Y ALFABETIZACIÓN MEDIÁTICA",
  "year": 2024,
  "venue": "Revista Ibero-Americana de Humanidades, Ciências e Educação",
  "abstract": "Literacia midiática é a área de pesquisa associada ao debate acadêmico e à intervenção social que incorpora elementos de alfabetização midiática, visando o estímulo ao pensamento crítico. Seu objetivo é oferecer reflexões e instrumentos para que cidadãos possam interpretar e produzir informações e conhecimento de forma crítica e ética. Esta pesquisa visa avaliar os níveis de literacia de um grupo de alunos e professores de Minas Gerais (MG). Um questionário online de múltipla escolha foi utilizado para coleta de dados. Correlações significativas foram encontradas entre literacia midiática e Fake News, “fonte confiável” e “informação confiável”. As mídias preferidas foram X-Twitter, Instagram e YouTube. Quanto à identificação de notícias falsas, temas científicos, como vacinação, mudança climática e efeito estufa tiveram maior destaque. As questões levantadas nesta pesquisa se relacionam à importância da literacia midiática, não apenas como antídoto ao vírus das Fake News, mas como forma de desenvolver o pensamento crítico em alunos e professores. Isto significa dizer que a educação crítica midiática transcende a mera habilitação em Tecnologias da Informação e Comunicação, envolvendo a identificação de conteúdo falso, a avaliação de notícias tendenciosas e a confiabilidade das informações veiculadas nas redes sociais.",
  "reason": "Questionário online com alunos e professores de Minas Gerais sobre literacia midiática e fake news."
 },
 {
  "id": "C86",
  "title": "Fake news pra quê? FAKE NEWS FOR WHAT? PERFORMANCE OF THE SCHOOL LIBRARY IN THE PROJECT TO COMBAT FAKE NEWS",
  "year": 2024,
  "venue": "BIBLOS",
  "abstract": "A pesquisa consiste em apresentar o resultado da aplicação do projeto “Fake News pra quê?” realizado com alunos do 8º ano de uma escola básica municipal da cidade de Biguaçu, estado de Santa Catarina. O projeto, elaborado pela bibliotecária da escola, autora deste artigo, foi implementado em parceria com a professora de português da escola. Neste sentido o artigo demonstra o papel do bibliotecário escolar no enfrentamento às fake news. O projeto aconteceu em 8 (oito) etapas, correspondentes a oito aulas, nas quais a bibliotecária teve participação ativa nas discussões e nos momentos de pesquisa. Finalizado o projeto, foi possível observar o comprometimento e interesse dos alunos pela temática apresentada e ao realizar as atividades propostas. O projeto proporcionou aos alunos o contato com informações falsas e suas consequências, permitiu a leitura e escrita e ainda trabalhou a competência em informação dos alunos.",
  "reason": "Projeto com alunos do 8º ano em escola municipal de Biguaçu (SC) sobre fake news e competência em informação, conduzido pela bibliotecária escolar."
 },
 {
  "id": "C31",
  "title": "Letramento midiático em desertos de notícias",
  "year": 2025,
  "venue": "Revista ECO-Pós",
  "abstract": "O Nordeste é a região com o maior número de desertos de notícias no Brasil, com o Piauí e do Rio Grande do Norte liderando em municípios classificados como vazios noticiosos. A ausência dessa cobertura local favorece a (re)circulação de conteúdos não verificados, tornando iniciativas como a COAR Notícias ( de fact-checking de incentivo ao letramento midiático) necessárias e urgentes. Este artigo objetiva aplicar o Arriégua: Manual de Checagem Nordestina em salas de aula da cidade de Itaueira (Piauí), categorizada como um deserto de notícias. Para tanto, foi realizado um estudo deste caso a partir de uma pesquisa survey com 53 estudantes e professores deste município. O estudo revelou que quase metade não possui o letramento necessário para compreender o processo de produção da notícia, a importância de ferramentas acessíveis de checagem, sobretudo em coberturas locais.",
  "reason": "Survey com estudantes e professores de uma cidade do Piauí sobre letramento midiático e checagem em sala de aula."
 },
 {
  "id": "C93",
  "title": "Perceptions of University Students in Communication about Disinformation:",
  "year": 2024,
  "venue": "Observatorio (OBS*)",
  "abstract": "This exploratory research is framed in the context of information disorders and its main objective is to identify the perception of Communication students in Brazil, Colombia and Spain about disinformation, their information consumption practices and aspects of their university education on media literacy. In order to carry out this study, an online survey was conducted between May and July 2023 in 23 higher education centers in the three countries, answered by 231 students. The main findings indicate that university students are aware of what fake news are and most of them know how to identify disinformative content, despite the fact that the development of the necessary skills for a critical reading of the media and the fight against disinformation takes place transversally in different subjects according to the students' perception, which shows the absence of a specific subject on media literacy in the curricula of the Communication degrees in the institutions assessed in the three countries.",
  "reason": "Survey com 231 estudantes de Comunicação do Brasil, Colômbia e Espanha, o que inclui amostra brasileira, sobre desinformação e formação em literacia midiática."
 },
 {
  "id": "C05",
  "title": "Educação midiática no combate à desinformação:",
  "year": 2025,
  "venue": "Revista TEIAS",
  "abstract": "Este artigo discute a educação midiática no combate à desinformação. Sua relevância está em refletir sobre o modo como as tecnologias digitais de informação e comunicação se fazem presente de forma negativa em nosso cotidiano e como a educação midiática pode ser inserida e aplicada no contexto escolar. Assim, tem como objetivo situar em que termos, na percepção dos professores, a desinformação tem chegado na escola, e quais proposições têm sido desenvolvidas com vistas a combatê-las, na perspectiva de uma educação midiática. Trata-se de uma pesquisa de natureza qualitativa. Inicialmente discutiu-se teoricamente as fake news como um fenômeno midiático presente no tempo e espaço atual de forma mais consubstancial e, em vista disso, a educação midiática como um caminho possível. Em seguida, realizou-se uma pesquisa de campo com professores da rede básica de ensino, utilizando questionário online como instrumento de produção dos dados. Como resultados, os professores percebem as implicações pessoais, sociais e pedagógicas da chegada da fake news na escola e vislumbram ações convencionais, porém válidas, na promoção de uma educação para/com/sobre as mídias.",
  "reason": "Pesquisa de campo com questionário online aplicado a professores da educação básica brasileira sobre desinformação na escola e educação midiática."
 },
 {
  "id": "C23",
  "title": "FORMAÇÃO INICIAL DE PROFESSORES E A DESINFORMAÇÃO: O PAPEL TRANSFORMADOR DA EDUCAÇÃO MIDIÁTICA",
  "year": 2025,
  "venue": "Areté.",
  "abstract": "O presente artigo disserta sobre o impacto da era digital na disseminação da desinformação e destaca o papel da educação, especialmente na formação inicial de professores, como recurso de enfrentamento desse fenômeno. A partir de uma pesquisa qualitativa com estudantes de Licenciatura em Informática Educacional, o estudo teve como objetivo verificar ambientes, na formação inicial de professores, que promovessem práticas e estudos sobre o contexto da sociedade permeada por informações falsas, manipuladas e/ou descontextualizadas e de como as mídias digitais favorecem a circulação desse tipo de conteúdo. O artigo propõe a educação midiática como estratégia essencial, defendendo a capacitação crítica e colaborativa dos professores em formação. Conclui-se que a educação, embora não resolva sozinha o problema, é pilar fundamental na construção de uma sociedade crítica e informada.",
  "reason": "Pesquisa qualitativa com licenciandos brasileiros sobre desinformação e educação midiática na formação inicial."
 },
 {
  "id": "C22",
  "title": "Educação midiática para notícias: histórico e mapeamento de iniciativas para combater a desinformação por meio da educação",
  "year": 2019,
  "venue": "Revista Mídia e Cotidiano",
  "abstract": "Este artigo discute o conceito de educação midiática à luz dos problemas trazidos pela disseminação de conteúdos falsos no ambiente digital. Além disso, apresenta um histórico da educação midiática nos Estados Unidos e um mapeamento de ações no Brasil, e apresenta achados de uma pesquisa realizada com professores/as de educação básica. Conclui-se que a preocupação em relação à educação midiática para notícias precisa ser apoiada pela comunidade escolar, sob pena de as futuras gerações viverem em uma sociedade em que as ciências como conhecimento compartilhado sejam desacreditadas, bem como a própria escola como instância em que este conhecimento é ensinado.",
  "reason": "Mapeamento de iniciativas e pesquisa com professores da educação básica brasileira sobre educação midiática para notícias falsas. A parte empírica é menos detalhada."
 },
 {
  "id": "C25",
  "title": "Desinformação e Ensino Superior: o papel das fake news na imagem das Instituições Federais de Ensino Superior (Ifes)",
  "year": 2025,
  "venue": "Ciência &amp; Educação (Bauru)",
  "abstract": "Resumo As notícias falsas têm capacidade de provocar prejuízos a diferentes segmentos da sociedade, em especial, à difamação da imagem de pessoas e organizações. Nos últimos anos, observaram-se diversas manchetes com informações falsas que questionaram a relevância das universidades públicas no Brasil. Diante de tal fato, este estudo buscou compreender em que medida as fake news têm impactado a reputação das Instituições Federais de Ensino Superior (Ifes). Para tal, fez-se uma investigação quantitativa com 307 estudantes do terceiro ano do Ensino Médio. Os resultados apresentaram associação estatisticamente significativa entre acreditar em fake news e a avaliação negativa das universidades públicas. A análise revelou ainda que a intensidade da adesão às notícias falsas indica forte magnitude na escolha de não cursar o Ensino Superior nas Ifes. As conclusões reforçam a importância da aprovação de legislações regulatórias da internet, bem como da inclusão do letramento informacional e midiático nos currículos escolares.",
  "reason": "Estudo quantitativo com 307 estudantes brasileiros do Ensino Médio sobre fake news, com recomendação de letramento midiático. O componente educacional é menos central."
 },
 {
  "id": "C108",
  "title": "Fake news no Facebook",
  "year": 2020,
  "venue": "Biblionline",
  "abstract": "No século XXI, o sentido do termo “fake news” tem forte relação com a propagação rápida de informação na internet feita, principalmente, por meio das redes sociais. Com base nisso, o objetivo deste trabalho foi verificar se os acadêmicos da Universidade Federal do Rio Grande (FURG), ao se depararem com uma informação, na rede social Facebook, recorrem a fontes de informação para se certificar sobre sua veracidade. Os objetivos específicos, por sua vez, foram os seguintes: a) identificar a frequência de acesso na rede social Facebook dos acadêmicos da FURG; b) verificar o número médio de compartilhamento de informações; c) especificar em que casos os usuários do Facebook verificam as informações recebidas, quanto à veracidade; d) investigar os critérios de escolha de fonte de informação. Quanto aos procedimentos metodológicos, o presente estudo teve como campo empírico a FURG e, como instrumento de pesquisa, seus universitários. Trata-se de um estudo de caso, de abordagem qualitativa, de natureza básica e caráter descritivo. Para a coleta de dados, foi utilizado o questionário impresso, com seis perguntas fechadas e quatro perguntas abertas e que foi aplicado na Biblioteca Central, localizada no Campus Carreiros. Com relação ao referencial teórico, foram apresentados conceitos e exemplos sobre fake news dentro das redes sociais, principalmente no Facebook, rede social aqui estudada. Os resultados mostram que um número significativo de universitários utiliza o Facebook como fonte de informação e que costumam fazer compartilhamentos. Porém, não se certificam das informações, quanto à veracidade, confiando apenas em fontes tradicionais de informação. Além disso, eles não se informam por meio das mídias independentes e portais informais. Diante disso, conclui-se que embora a fonte de informação seja relevante para os universitários, eles precisam ser educados a investigar criteriosamente a informação em si, além da sua fonte.",
  "reason": "Questionário com universitários da FURG sobre verificação de informações no Facebook e fake news. A relação com competência em informação é moderada."
 },
 {
  "id": "C94",
  "title": "ALFABETIZAÇÃO CIENTÍFICA, ALFABETIZAÇÃO MIDIÁTICA E ILHOTAS INTERDISCIPLINARES DE RACIONALIDADE: UMA VIVÊNCIA EM DIDÁTICA DAS CIÊNCIAS",
  "year": 2022,
  "venue": "Revista Vitruvian Cogitationes",
  "abstract": "O presente artigo objetiva narrar, de forma descritiva e analítica, a vivência em uma oficina didática em que foi desenvolvida a estratégia teórico-metodológica, denominada Ilhota Interdisciplinar de Racionalidade, em uma disciplina de Didática das Ciências, de um curso de formação inicial de professores em Ciências Exatas. O desenvolvimento decorre da necessidade de formar professores com conhecimentos profissionais que lhes permitam atuar no contexto atual, de pandemia e pós-pandemia, em que notícias falsas, as fake news, desinformam as pessoas. Ao analisar, com um olhar qualitativo, os diários de campo de uma das licenciandas participantes, observou-se como a metodologia pode contribuir para a formação de professores e em prol da alfabetização científica e midiática na Educação em Ciências. As atividades foram realizadas de forma remota, utilizando plataformas virtuais para o desenvolvimento das atividades. Apesar das dificuldades e limitações do distanciamento social, infere-se que a prática metodológica permitiu o desenvolvimento de autonomia docente, reflexão didático - pedagógica e compreensões acerca das relações entre alfabetização científica e interdisciplinaridade.",
  "reason": "Relato de oficina em disciplina de formação de professores, com análise de diários de campo, sobre alfabetização científica e midiática diante de fake news. O contexto pandêmico não é o foco."
 },
 {
  "id": "C97",
  "title": "A importância da alfabetização científica no combate a disseminação de notícias falsas",
  "year": 2024,
  "venue": "Contribuciones a las Ciencias Sociales",
  "abstract": "A divulgação de notícias falsas, existe em todos os períodos históricos, porém no Brasil teve seu maior enfrentamento no período das eleições de 2018 e 2022 intercalada pela pandemia do Covid 19. Coincidentemente, nos últimos anos as alterações na LDB vêm trazendo a importância da alfabetização científica, desde os anos iniciais da educação básica. Com o objetivo em compreender a relação da alfabetização na detecção e no combate das notícias falsas, desenvolveu-se o presente estudo. Para isso, foram selecionadas duas escolas, uma pública e uma privada e as três turmas do ensino médio, onde um questionário foi aplicado para 51 alunos de cada escola, com a finalidade de perceber uma relação da modalidade de ensino, idade e realidades socioeconômicas distintas à detecção e combate de fake news. Foi verificado que a frequência de notícias falsas era maior na escola privada do que na pública, porém a busca pela informação correta independe entre as séries e entre as escolas. Sugerindo um reflexo positivo da alfabetização científica no combate à fake news.",
  "reason": "Questionário com alunos do ensino médio de escola pública e privada sobre detecção de fake news e alfabetização científica. A ligação com letramento midiático é indireta."
 },
 {
  "id": "C124",
  "title": "DE MEMES A FAKE NEWS",
  "year": 2020,
  "venue": "Educação em Foco",
  "abstract": "O presente artigo é uma análise dos achados de uma pesquisa- -formação que acontece no programa de pós-graduação em educação da UFRRJ, que tem como campo de pesquisa o cotidiano da disciplina de “Informática na Educação” do curso de Licenciatura em Pedagogia a distância pela UERJ/CEDERJ/UAB. Nosso objetivo era compreender quais os usos que os praticantes culturais fazem de seus dispositivos móveis e como são instituídas as práticas de App-Learning em seu cotidiano para formar docentes na Cibercultura. Partimos desse contexto para pesquisar a emergência das fake news e suas repercussões na sociedade, inclusive na educação, para propor estratégias e metodologias de pesquisa-formação em tempos de pós-verdade (SANTAELLA).",
  "reason": "Pesquisa-formação em disciplina de Pedagogia a distância sobre fake news e formação docente. O resumo descreve o método de forma vaga."
 },
 {
  "id": "C78",
  "title": "Redes sociais, política e desinformação: Uma análise da circulação de Fake News entre universitários brasileiros Social Networks, Politics, and Disinformation: An Analysis of the Circulation of Fake News among Brazilian University Students",
  "year": 2025,
  "venue": "RCMOS - Revista Científica Multidisciplinar O Saber",
  "abstract": "This article examines the circulation of fake news among Brazilian university students, considering the role of social networks, political polarization, and contemporary dynamics of disinformation. Although they have higher levels of education and broad access to information, students are also exposed to algorithms that reinforce digital echo chambers and to the emotional appeal of conspiracy theories. The study adopts an exploratory-descriptive approach, combining a literature review with a survey conducted through snowball sampling. The questionnaire investigated informational habits, exposure to false content, self-reported sharing of misleading news, and adherence to conspiracy narratives. The results indicate strong dependence on social networks as a primary source of news, distrust of traditional media, and the influence of factors such as political positioning and religiosity on the propensity to believe or disseminate disinformation. The study highlights the need to strengthen media literacy and critical information skills to confront disinformation within the university environment.",
  "reason": "Survey com universitários brasileiros sobre circulação de fake news, com conclusão voltada à literacia midiática. O foco educacional é secundário e o tema envolve política."
 }
]