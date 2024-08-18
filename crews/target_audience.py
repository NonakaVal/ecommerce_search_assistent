from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

def create_target_audience_analysis_team(product_name, llm):

    max_iter = 25
    
    # Definir Agentes
    audience_research_expert = Agent(
        role="Especialista em Pesquisa de Público-Alvo",
        goal=f"""Coletar e analisar dados sobre o público-alvo de {product_name}, incluindo demografia, comportamentos de compra, 
                 preferências e necessidades.""",
        backstory=f"""Especialista em pesquisa de mercado, com foco em entender o perfil demográfico e psicográfico dos consumidores 
                      de {product_name}. Esse agente se dedica a reunir dados relevantes e interpretar as necessidades do público-alvo.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    buyer_persona_creator = Agent(
        role="Criador de Persona de Comprador",
        goal=f"""Desenvolver personas detalhadas para o público-alvo de {product_name}, com base em dados coletados e analisados.""",
        backstory=f"""Especialista em criação de personas, responsável por transformar dados sobre o público-alvo em perfis detalhados e 
                      representativos de clientes ideais para {product_name}. Essas personas ajudarão a direcionar estratégias de marketing.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    behavior_analysis_specialist = Agent(
        role="Especialista em Análise Comportamental",
        goal=f"""Analisar o comportamento do público-alvo em relação a {product_name}, identificando padrões de compra, preferências e 
                 fatores que influenciam a decisão de compra.""",
        backstory=f"""Especialista em comportamento do consumidor, com experiência em identificar e analisar padrões e tendências que 
                      afetam as decisões de compra do público-alvo de {product_name}.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    market_segment_expert = Agent(
        role="Especialista em Segmentação de Mercado",
        goal=f"""Segmentação detalhada do mercado para {product_name}, identificando diferentes grupos dentro do público-alvo com base 
                 em características e comportamentos similares.""",
        backstory=f"""Com experiência em segmentação de mercado, este agente foca em identificar e descrever diferentes segmentos dentro 
                      do público-alvo de {product_name}, facilitando a criação de estratégias de marketing personalizadas.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Coletar e compilar dados demográficos e psicográficos sobre o público-alvo de {product_name}. O relatório deve incluir:
                        1. Idade, gênero, localização e nível educacional
                        2. Comportamentos de compra e preferências
                        3. Necessidades e desafios
                        4. Fontes de informação e influências""",
        expected_output="Relatório detalhado sobre o perfil do público-alvo.",
        agent=audience_research_expert
    )

    task2 = Task(
        description=f"""Desenvolver personas detalhadas para o público-alvo de {product_name}. As personas devem incluir:
                        1. Nome e foto fictícia
                        2. Demografia e psicografia
                        3. Objetivos e desafios
                        4. Comportamentos de compra e preferências
                        5. Fontes de informação e influências""",
        expected_output="Perfis detalhados de personas do público-alvo.",
        agent=buyer_persona_creator
    )

    task3 = Task(
        description=f"""Analisar o comportamento de compra do público-alvo de {product_name}. O relatório deve cobrir:
                        1. Padrões de compra e preferências
                        2. Influências nas decisões de compra
                        3. Barreiras e incentivos
                        4. Tendências emergentes""",
        expected_output="Relatório sobre comportamento de compra e influências.",
        agent=behavior_analysis_specialist
    )

    task4 = Task(
        description=f"""Segregar o mercado para {product_name} em diferentes segmentos com base em características e comportamentos. O relatório 
                        deve incluir:
                        1. Definição dos segmentos de mercado
                        2. Características e necessidades de cada segmento
                        3. Potencial de mercado e estratégias recomendadas""",
        expected_output="Relatório sobre segmentação de mercado e estratégias associadas.",
        agent=market_segment_expert
    )

    # Criar e Executar a Equipe
    target_audience_crew = Crew(
        agents=[audience_research_expert, buyer_persona_creator, behavior_analysis_specialist, market_segment_expert],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = target_audience_crew.kickoff()
    return crew_result

def create_customer_retention_team(product_name, llm):

    max_iter = 50

    # Definir Agentes
    retention_analysis_expert = Agent(
        role="Especialista em Análise de Retenção de Clientes",
        goal=f"""Analisar as taxas de retenção de clientes para {product_name} e identificar os principais motivos de perda de clientes.""",
        backstory=f"""Especialista em analisar e melhorar taxas de retenção de clientes. Experiente na identificação de motivos de perda e em desenvolver estratégias para aumentar a fidelidade dos clientes para produtos como {product_name}.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    customer_churn_analyst = Agent(
        role="Analista de Churn de Clientes",
        goal=f"""Identificar e analisar os principais fatores que contribuem para o churn de clientes de {product_name}, e sugerir ações para reduzir a perda de clientes.""",
        backstory=f"""Com experiência em analisar a perda de clientes e seus fatores contribuintes, este especialista fornece insights para minimizar o churn e melhorar a retenção de clientes para {product_name}.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    feedback_analysis_specialist = Agent(
        role="Especialista em Análise de Feedback de Clientes",
        goal=f"""Coletar e analisar feedback de clientes para entender os motivos de insatisfação e perda, fornecendo recomendações para melhorar a experiência do cliente com {product_name}.""",
        backstory=f"""Especialista em interpretar feedback de clientes para identificar áreas de melhoria e entender as causas da insatisfação e perda de clientes. Experiente em traduzir feedback em ações práticas para retenção de clientes.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    retention_strategy_developer = Agent(
        role="Desenvolvedor de Estratégias de Retenção",
        goal=f"""Desenvolver e implementar estratégias para melhorar as taxas de retenção de clientes para {product_name}, com base nas análises e feedbacks recebidos.""",
        backstory=f"""Especialista em criar e aplicar estratégias de retenção de clientes, com foco em aumentar a fidelidade e reduzir a perda de clientes para produtos como {product_name}. Experiente em transformar dados e análises em ações concretas para retenção.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Analisar as taxas de retenção de clientes para {product_name} e identificar os principais motivos de perda. O relatório deve incluir:
                        1. Taxas de retenção por segmento de mercado
                        2. Principais motivos de perda de clientes
                        3. Comparação com taxas de retenção de concorrentes
                        4. Tendências de retenção ao longo do tempo
                        5. Sugestões para melhorar a retenção de clientes""",
        expected_output="Relatório detalhado sobre taxas de retenção e motivos de perda de clientes.",
        agent=retention_analysis_expert,
    )

    task2 = Task(
        description=f"""Identificar os principais fatores que contribuem para o churn de clientes de {product_name} e sugerir ações para reduzir a perda. O relatório deve abordar:
                        1. Fatores principais do churn
                        2. Análise de clientes que deixaram o produto
                        3. Comparação com benchmarks de mercado
                        4. Estratégias de mitigação para reduzir o churn
                        5. Recomendações de melhoria""",
        expected_output="Relatório sobre fatores de churn e estratégias para redução.",
        agent=customer_churn_analyst,
    )

    task3 = Task(
        description=f"""Coletar e analisar feedback de clientes sobre {product_name} para entender motivos de insatisfação e perda. O relatório deve incluir:
                        1. Principais elogios e críticas
                        2. Sugestões de melhorias
                        3. Pontos fortes e fracos percebidos
                        4. Impacto das críticas na retenção
                        5. Insights para aprimoramento do produto""",
        expected_output="Relatório detalhado sobre feedback de clientes e sugestões de melhoria.",
        agent=feedback_analysis_specialist,
    )

    task4 = Task(
        description=f"""Desenvolver estratégias detalhadas para melhorar as taxas de retenção de clientes para {product_name}. O plano deve incluir:
                        1. Ações para aumentar a fidelidade
                        2. Planos de ação para abordar feedbacks negativos
                        3. Medidas para melhorar a experiência do cliente
                        4. Monitoramento e ajustes contínuos
                        5. Implementação de melhores práticas de retenção""",
        expected_output="Plano estratégico detalhado para retenção de clientes.",
        agent=retention_strategy_developer,
        context=[task1, task2, task3]
    )

    # Criar e Executar a Equipe
    customer_retention_crew = Crew(
        agents=[retention_analysis_expert, customer_churn_analyst, feedback_analysis_specialist, retention_strategy_developer],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = customer_retention_crew.kickoff()
    return crew_result
