from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

def create_crewai_setup(product_name, llm):

    max_iter = 50

    # Definir Agentes
    market_research_analyst = Agent(
        role="Analista de Pesquisa de Mercado",
        goal=f"""Analisar a demanda de mercado para {product_name} e 
                 sugerir estratégias de marketing""",
        backstory=f"""Especialista em entender a demanda de mercado, público-alvo, 
                      e concorrência para produtos como {product_name}. 
                      Hábil em desenvolver estratégias de marketing 
                      para alcançar um amplo público.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter =max_iter
    
    )

    customer_behavior_expert = Agent(
        role="Especialista em Comportamento do Consumidor",
        goal=f"""Analisar as preferências e comportamentos de compra do público-alvo de {product_name}, 
                 identificando as principais motivações de compra.""",
        backstory=f"""Com vasta experiência no estudo de comportamentos de consumo e 
                      análise de padrões de compra, este especialista identifica como e por que 
                      os consumidores compram produtos como {product_name}.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter =max_iter
    )

    competitor_analysis_specialist = Agent(
        role="Especialista em Análise de Concorrência",
        goal=f"""Avaliar a concorrência direta e indireta de {product_name}, 
                 identificando as estratégias usadas pelos principais competidores 
                 para capturar e manter a demanda no mercado.""",
        backstory=f"""Especializado em análise competitiva, com foco em estudar concorrentes, 
                      suas ofertas, estratégias de marketing e como se posicionam no mercado 
                      para atender à demanda existente.""",
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True,
        allow_delegation=True,
        llm=llm,
        max_iter =max_iter
    )

    trend_analysis_expert = Agent(
        role="Especialista em Análise de Tendências",
        goal=f"""Analisar as tendências emergentes relacionadas a {product_name} e como essas tendências 
                 podem impactar a demanda futura do produto.""",
        backstory=f"""Especialista em identificar e interpretar tendências de mercado e como elas 
                      afetam a demanda por produtos como {product_name}. Hábil em prever como 
                      as tendências futuras podem influenciar o mercado.""",
        verbose=True,
        allow_delegation=True,
        llm=llm,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        max_iter =max_iter
    )

    customer_feedback_analyst = Agent(
        role="Analista de Feedback de Clientes",
        goal=f"""Coletar e analisar o feedback dos clientes sobre produtos similares a {product_name}, 
                 para entender suas preferências, insatisfações e sugestões de melhorias.""",
        backstory=f"""Experiente em coleta e análise de feedback de clientes, este especialista é 
                      hábil em interpretar comentários, avaliações e sugestões para melhorar 
                      a aceitação e demanda por produtos como {product_name}.""",
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],   
        verbose=True,
        allow_delegation=True,
        llm=llm,
        max_iter =max_iter
    )
    
    secondary_data_researcher = Agent(
        role="Pesquisador de Dados Secundários",
        goal=f"""Recolher e analisar dados secundários relevantes para {product_name}, como relatórios 
                 de mercado existentes, estudos de caso e dados estatísticos que possam oferecer 
                 insights adicionais sobre a demanda.""",
        backstory=f"""Especialista em pesquisa e análise de dados secundários, com habilidade para 
                      extrair e interpretar informações de relatórios de mercado, estudos acadêmicos 
                      e outras fontes de dados que forneçam uma visão abrangente sobre a demanda de mercado.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],  
        allow_delegation=True,
        llm=llm,
    )

    strategic_planner = Agent(
        role="Planejador Estratégico",
        goal=f"""Desenvolver planos estratégicos detalhados com base nas análises da equipe principal e do analista de dados avançados. 
                 Focar em ações práticas para maximizar o impacto das recomendações no mercado para {product_name}.""",
        backstory=f"""Com vasta experiência em planejamento estratégico, este especialista transforma análises em planos de ação concretos 
                      e implementáveis, visando melhorar a posição de mercado e otimizar estratégias de marketing e vendas.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],   
        llm=llm,
        max_iter=max_iter
    )

    impact_evaluator = Agent(
        role="Avaliador de Impacto Estratégico",
        goal=f"""Avaliar o impacto das estratégias propostas e das tendências emergentes sobre o mercado para {product_name}. 
                 Prever como as mudanças recomendadas podem afetar a demanda e ajustar as estratégias conforme necessário.""",
        backstory=f"""Especialista em avaliação de impacto com habilidade para prever como as estratégias e tendências impactam o mercado. 
                      Experiência em ajustar estratégias para maximizar a eficácia e atender às necessidades do mercado.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],  
        llm=llm,
        max_iter=max_iter
    )



    # Definir Tarefas
    task1 = Task(
        description=f"""Analisar a demanda de mercado para {product_name}. O mês atual é Jan 2024.
                        Escrever um relatório sobre o perfil ideal do cliente e estratégias de 
                        marketing para alcançar o maior público possível. 
                        Incluir pelo menos 10 pontos abordando áreas-chave de marketing.""",

        expected_output="Relatório sobre análise de demanda de mercado e estratégias de marketing.",
        agent=market_research_analyst,
    )

    task2 = Task(
        description=f"""Analisar as preferências e comportamentos de compra do público-alvo de {product_name} , 
                        com foco em entender as motivações e barreiras de compra. Identificar os principais fatores , O mês atual é Jan 2024.
                        que influenciam a decisão de compra.
                        Incluir pelo menos 10 pontos abordando áreas-chave sobre o comportamentos de compra do público-alvo de {product_name}.
                        """,

        expected_output="Relatório detalhado sobre comportamento de compra dos consumidores, abordando todos os tópicos",
        agent=customer_behavior_expert,

    )

    task3 = Task(
        description=f"""Realizar uma análise competitiva para {product_name}, identificando os principais competidores, 
                        suas estratégias de marketing e como atendem à demanda no mercado atual,  O mês atual é Jan 2024.
                        Incluir pelo menos 10 pontos abordando áreas-chave sobre o mercado de {product_name}.
                        """,
        expected_output="Relatório sobre análise de concorrência e diferenciação no mercado, abordando todos os tópicos",
        agent=competitor_analysis_specialist,

    )

    task4 = Task(
        description=f"""Analisar as tendências emergentes para {product_name} em Janeiro de 2024. O relatório deve abordar:
        1. Tendências tecnológicas
        2. Mudanças no comportamento do consumidor
        3. Impacto de novas regulamentações
        4. Avanços econômicos e demanda
        5. Alterações no mercado global e local
        6. Inovações em produtos e serviços
        7. Previsões de crescimento do mercado
        8. Dinâmica competitiva
        9. Tendências culturais
        10. Oportunidades e riscos associados""",
        expected_output="Relatório detalhado sobre tendências emergentes e seu impacto na demanda, cobrindo todos os tópicos.",
        agent=trend_analysis_expert,

    )


    task5 = Task(
        description=f"""Coletar e analisar feedback de clientes sobre produtos similares a {product_name},  O mês atual é Jan 2024.
                        O relatório deve responder os seguintes tópicos:
                        1. Principais elogios e críticas
                        2. Sugestões de melhorias dos clientes
                        3. Pontos fortes percebidos pelos consumidores
                        4. Problemas recorrentes identificados
                        5. Níveis de satisfação geral
                        6. Comparação de feedback com produtos concorrentes
                        7. Análise de tendências no feedback
                        8. Impacto das críticas nas decisões de compra
                        9. Preferências dos consumidores em relação a características do produto
                        10. Insights para aprimoramento do produto""",
        expected_output="Relatório sobre feedback de clientes e sugestões de melhoria.",
        agent=customer_feedback_analyst,
    )
    
    task6 = Task(
        description=f"""Recolher e analisar dados secundários relevantes para {product_name}, como relatórios 
                        de mercado existentes, estudos de caso e dados estatísticos que possam oferecer 
                        insights adicionais sobre a demanda. Utilizar essas informações para complementar 
                        a análise primária e fornecer uma visão mais completa.

                        O relatório deve responder os seguintes tópicos:
                        1. Resumo dos principais relatórios de mercado
                        2. Dados estatísticos relevantes
                        3. Estudos de caso relevantes
                        4. Tendências identificadas em dados secundários
                        5. Insights adicionais sobre a demanda de mercado
                        6. Comparação de dados primários e secundários
                        7. Análise de lacunas nos dados existentes
                        8. Impacto dos dados secundários na análise de demanda
                        9. Relevância dos dados secundários para a estratégia de mercado
                        10. Sugestões baseadas nos dados secundários""",
        expected_output="Relatório sobre dados secundários e como eles impactam a análise de demanda.",
        agent=secondary_data_researcher,
    )


    task7 = Task(
    description=f"""Desenvolver planos estratégicos detalhados com base nas análises e insights da equipe principal e do analista de dados avançados. 
                    Incluir recomendações práticas e estratégias para melhorar a posição de mercado de {product_name}. O mês atual é Jan 2024.""",
    expected_output="Plano estratégico detalhado com recomendações práticas e ações a serem implementadas.",
    agent=strategic_planner,
    context= [task1,task2,task3,task4, task5, task6]

    )

    task8 = Task(
        description=f"""Avaliar o impacto das estratégias propostas e das tendências emergentes sobre o mercado para {product_name}. 
                        Prever como essas mudanças podem afetar a demanda e ajustar as estratégias conforme necessário. O mês atual é Jan 2024.""",
        expected_output="Relatório sobre o impacto potencial das estratégias e tendências, com recomendações de ajustes.",
        agent=impact_evaluator,
        context= [task1,task2,task3,task4, task5, task6, task7]
    )

    # Criar e Executar a Equipe
    product_crew = Crew(
        agents=[market_research_analyst, customer_behavior_expert, competitor_analysis_specialist, 
                trend_analysis_expert, customer_feedback_analyst, secondary_data_researcher,strategic_planner, impact_evaluator],
        tasks=[task1, task2, task3, task4, task5,task6, task7,task8],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = product_crew.kickoff()
    return crew_result




def create_crewai_setup_2(product_name, llm):

    # Especialista em Estratégia de Marketing
    marketing_strategist = Agent(
        role='Especialista em Estratégia de Marketing',
        goal=f'Identificar e validar as melhores estratégias e fontes online para melhorar o marketing relacionado a {product_name}.',
        backstory=f'Com vasta experiência em estratégias de marketing, este agente é capaz de encontrar e validar fontes confiáveis sobre práticas e tendências de marketing.',
        llm=llm,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True,
    )

    # Consultor de Marketing
    marketing_consultant = Agent(
        role='Consultor de Marketing',
        goal=f'Definir novas estratégias de marketing baseadas em pesquisas e validar as melhores práticas e fontes relacionadas a {product_name}.',
        backstory=f'Especialista em desenvolvimento de estratégias de marketing, este agente identifica lacunas e propõe novas direções para melhorar as práticas de marketing sobre {product_name}.',
        llm=llm,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True,
    )

    # Analista de Mercado
    market_analyst = Agent(
        role='Analista de Mercado',
        goal=f'Coletar dados de fontes online sobre estratégias de marketing e organizá-los para uma análise detalhada sobre {product_name}.',
        backstory=f'Especialista em coleta e organização de dados de marketing, este agente é responsável por reunir informações úteis e precisas para análise estratégica.',
        llm=llm,
        verbose=True,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
    )

    # Analista de Dados de Marketing
    marketing_data_analyst = Agent(
        role='Analista de Dados de Marketing',
        goal=f'Analisar dados coletados sobre estratégias de marketing, extraindo insights e criando um relatório detalhado sobre {product_name}.',
        backstory=f'Especialista em análise de dados de marketing, com habilidades para elaborar relatórios detalhados e precisos a partir de informações coletadas.',
        llm=llm,
        verbose=True,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
    )

    # Revisor de Estratégias de Marketing
    marketing_reviewer = Agent(
        role='Revisor de Estratégias de Marketing',
        goal=f'Revisar e validar as estratégias de marketing e dados coletados, garantindo a precisão e relevância das informações sobre {product_name}.',
        backstory=f'Especialista em revisão de estratégias de marketing, este agente assegura a qualidade e a precisão das estratégias e dados apresentados.',
        llm=llm,
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
    )

    # Redator de Estratégias de Marketing
    marketing_writer = Agent(
        role='Redator de Estratégias de Marketing',
        goal=f'Redigir um documento estratégico estruturado com base em dados e análises sobre {product_name}, apresentando as melhores práticas e recomendações.',
        backstory=f'Capaz de criar documentos claros e persuasivos sobre estratégias de marketing, este agente comunica descobertas e recomendações de forma eficaz.',
        llm=llm,
        verbose=True,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()]
    )


    # Tarefas# Tarefa de Gerenciamento de Estratégia de Marketing
    marketing_management_task = Task(
        description=f'Identificar e validar as melhores práticas e fontes online para melhorar o marketing relacionado a {product_name}.',
        expected_output=f'Documento detalhado que cubra todos os aspectos necessários para aprimorar as estratégias de marketing relacionadas a {product_name}.',
        agent=marketing_strategist,
    )

    # Tarefa de Coleta de Dados de Marketing
    data_collection_task = Task(
        description=f'Coletar dados atualizados sobre estratégias de marketing de fontes online validadas para responder precisamente à questão: {product_name}.',
        expected_output='Grande quantidade de dados coletados e preparados para análise estratégica.',
        agent=market_analyst,
        context=[marketing_management_task]
    )

    # Tarefa de Análise de Dados de Marketing
    data_analysis_task = Task(
        description=f'Analisar os dados coletados sobre estratégias de marketing, extraindo insights detalhados e relevantes sobre {product_name}.',
        expected_output=f'Lista de estratégias com as melhores e mais detalhadas respostas para a questão: {product_name}.',
        agent=marketing_data_analyst,
        context=[marketing_management_task, data_collection_task]
    )

    # Tarefa de Revisão de Estratégias
    data_review_task = Task(
        description=f'Revisar o material coletado e analisado sobre estratégias de marketing, garantindo precisão, consistência e relevância.',
        expected_output='Relatório detalhado com sugestões de melhoria e feedback crítico.',
        agent=marketing_reviewer,
        context=[data_analysis_task]
    )

    # Tarefa de Redação de Estratégias de Marketing
    article_writing_task = Task(
        description=f'Redigir um documento estratégico e estruturado, apresentando as melhores práticas e recomendações para {product_name}.',
        expected_output='Documento completo e estruturado com as melhores estratégias, links e explicações detalhadas.',
        agent=marketing_writer,
        async_execution=False,
        context=[marketing_management_task, data_collection_task, data_analysis_task, data_review_task],
    )

    # Tarefa de Novas Estratégias
    new_strategies_task = Task(
        description=f'Desenvolver novas estratégias de marketing relevantes com base nos achados sobre {product_name}.',
        expected_output='Lista de novas estratégias que precisam ser exploradas para avançar no marketing.',
        agent=marketing_consultant,
        context=[marketing_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task]
    )

    # Configurando a equipe (Crew)
    crew = Crew(
        agents=[marketing_strategist, marketing_consultant, market_analyst, marketing_data_analyst, marketing_reviewer, marketing_writer],
        tasks=[marketing_management_task, data_collection_task, data_analysis_task, data_review_task, article_writing_task, new_strategies_task],
        process=Process.sequential,  # Processo sequencial para execução das tarefas
        manager_llm=llm,  # Definindo o modelo LLM para gerenciar a equipe
        verbose=True
    )


    crew_result = crew.kickoff()
    return crew_result



def create_crewai_setup_3(product_name, llm):
    # Agentes
    market_research_manager = Agent(
        role='Gerente de Pesquisa de Mercado',
        goal='Liderar a pesquisa de mercado, identificando e validando as melhores fontes de dados de mercado.',
        backstory='Com ampla experiência em pesquisa de mercado, este agente é capaz de liderar projetos de pesquisa detalhados e abrangentes.',
        llm=llm,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose = True
    )

    competitive_analysis_expert = Agent(
        role=f'Especialista em Análise Competitiva e {product_name}',
        goal='Realizar análise detalhada dos cinco pontos da indústria: rivalidade competitiva, barreiras de entrada, ameaça de substituição, poder do comprador e poder do fornecedor.',
        backstory='Com experiência em análise competitiva, este agente é capaz de avaliar as dinâmicas da indústria e identificar fatores críticos.',
        llm=llm,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True
    )

    swot_analysis_expert = Agent(
        role='Especialista em Análise SWOT',
        goal='Conduzir análise SWOT detalhada para identificar forças, fraquezas, oportunidades e ameaças do mercado.',
        backstory='Especialista em análise estratégica, este agente pode identificar fatores internos e externos que impactam o mercado.',
        llm=llm,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True
    )

    buyer_analyst = Agent(
        role='Analista de Compradores',
        goal='Entender os compradores, incluindo fatos sobre o mercado-alvo, demandas, preços, percepção da concorrência, e impressões da marca.',
        backstory='Experiente em pesquisa de comportamento do consumidor, este agente pode fornecer insights detalhados sobre os compradores.',
        llm=llm,
        allow_delegation=False,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        verbose=True
    )

    # Tarefas
    industry_analysis_task = Task(
        description=f"""
        Realizar uma análise detalhada dos cinco pontos do mercado de {product_name}:
        1. **Rivalidade Competitiva**: Avaliar a intensidade da concorrência no mercado, incluindo número de concorrentes, estratégias competitivas, e participação de mercado.
        2. **Barreiras de Entrada**: Identificar as principais barreiras que novas empresas enfrentam ao entrar no mercado, como regulamentações, capital inicial, e acesso a recursos.
        3. **Ameaça de Substituição**: Analisar a presença e a ameaça de produtos ou serviços substitutos que podem reduzir a demanda pelo produto.
        4. **Poder do Comprador**: Avaliar o poder de negociação dos compradores, incluindo sua sensibilidade a preços, poder de barganha, e disponibilidade de alternativas.
        5. **Poder do Fornecedor**: Analisar o poder de negociação dos fornecedores, considerando fatores como número de fornecedores, disponibilidade de matérias-primas, e custo de mudança de fornecedor.
        """,
        expected_output=f"Relatório detalhado sobre os cinco pontos do mercado de {product_name} e venda de {product_name}.",
        agent=competitive_analysis_expert,
   
    )

    swot_analysis_task = Task(
        description=f"""
        Conduzir uma análise SWOT detalhada para identificar os seguintes aspectos do mercado de {product_name}:
        1. **Forças**: Identificar os pontos fortes e venda de {product_name}, como qualidade, marca, e vantagens competitivas.
        2. **Fraquezas**: Apontar as principais fraquezas e limitações, incluindo falta de recursos, pontos fracos operacionais, e áreas onde a concorrência supera a empresa.
        3. **Oportunidades**: Explorar oportunidades de crescimento e expansão no mercado, como novas tendências, mudanças no comportamento do consumidor, e áreas de inovação.
        4. **Ameaças**: Identificar ameaças externas que podem impactar negativamente o mercado e a empresa, como mudanças econômicas, novas regulamentações, e ações dos concorrentes.
        """,
        expected_output=f"Relatório detalhado de análise SWOT do {product_name}",
        agent=swot_analysis_expert,

    )

    buyer_understanding_task = Task(
        description=f"""
        Realizar uma análise abrangente para entender os compradores de {product_name}, abordando os seguintes aspectos:
        1. **Dados Demográficos e Psicográficos**: Coletar informações sobre as características demográficas (idade, gênero, localização) e psicográficas (interesses, estilo de vida) dos compradores.
        2. **Fatores Decisivos na Compra**: Identificar os principais fatores que influenciam a decisão de compra dos consumidores, como qualidade, preço, conveniência e características do produto.
        3. **Demanda pelo Produto**: Avaliar a demanda atual e projetada para {product_name}, considerando dados de mercado, tendências de consumo e comportamento dos compradores.
        4. **Faixas de Preço Aceitáveis**: Analisar a disposição dos compradores em pagar por diferentes faixas de preço e identificar o intervalo de preços mais aceitável e competitivo para {product_name}.
        5. **Percepção da Concorrência**: Investigar como os consumidores percebem a concorrência, identificando pontos fortes e fracos dos concorrentes em comparação com {product_name}.
        6. **Impressões da Marca**: Avaliar a percepção da marca {product_name} pelos consumidores, incluindo aspectos como confiança, lealdade, e imagem de marca.
        7. **Perfil Profissional dos Compradores**: Identificar as profissões mais comuns entre os compradores e entender como isso pode influenciar suas decisões de compra.
        8. **Rotina Diária dos Compradores**: Descrever um dia típico na vida dos compradores para entender melhor suas rotinas, hábitos e necessidades relacionadas ao produto.
        9. **Fontes de Informação sobre Produtos**: Determinar onde os compradores buscam informações sobre produtos e serviços, como mídias sociais, sites de resenha e recomendações de amigos.
        10. **Preferências de Compra**: Identificar as preferências dos compradores em relação à forma de aquisição, seja online, em lojas físicas ou por meio de outros canais.
        11. **Critérios de Seleção de Fornecedores**: Analisar os principais critérios que os compradores consideram ao escolher fornecedores, como preço, qualidade do atendimento, e reputação da empresa.
        """,
        expected_output=f"Relatório detalhado sobre compradores ideias de {product_name} , com foco em dados demográficos, psicográficos, e comportamentais.",
        agent=buyer_analyst,
        context=[industry_analysis_task, swot_analysis_task]
    )

    market_research_management_task = Task(
        description=f"""
        Coordenar e supervisionar todas as etapas da pesquisa de mercado para {product_name}, garantindo a precisão e relevância dos dados coletados. 
        As etapas incluem:
        1. **Definição de Objetivos**: Clarificar os objetivos específicos da pesquisa de mercado.
        2. **Planejamento da Pesquisa**: Desenvolver um plano detalhado, incluindo metodologias, fontes de dados, e cronograma.
        3. **Coleta de Dados**: Supervisionar a coleta de dados primários e secundários.
        4. **Análise de Dados**: Coordenar a análise dos dados coletados para gerar insights significativos.
        5. **Relatórios e Apresentações**: Preparar relatórios detalhados e apresentações dos resultados da pesquisa.
        6. **Validação dos Dados**: Garantir a validação dos dados e a precisão dos relatórios gerados.
        """,
        expected_output=f"Documento detalhado que cubra todos os tópicos necessários para responder a questão de pesquisa de mercado sobre {product_name}",
        agent=market_research_manager,
        context=[industry_analysis_task, buyer_understanding_task, swot_analysis_task],
    )

    # Configurando a equipe (Crew)
    crew = Crew(
        agents=[market_research_manager, competitive_analysis_expert, swot_analysis_expert, buyer_analyst],
        tasks=[industry_analysis_task, swot_analysis_task, buyer_understanding_task, market_research_management_task],
        process=Process.sequential,  # Processo sequencial para execução das tarefas
        manager_llm=llm,  # Definindo o modelo LLM para gerenciar a equipe
        verbose=True
    )

    # Iniciar a execução das tarefas
    crew_result = crew.kickoff()
    return crew
