from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

def create_product_detail_team(product_name, llm):

    max_iter = 25

    # Definir Agentes
    product_specification_expert = Agent(
        role="Especialista em Especificações de Produto",
        goal=f"""Coletar e analisar informações detalhadas sobre as especificações técnicas de {product_name}, 
                 identificando seus componentes, materiais, e desempenho.""",
        backstory=f"""Com vasta experiência em análise de especificações de produto, este especialista é capaz 
                      de identificar detalhes técnicos e de desempenho de {product_name}, oferecendo uma visão abrangente 
                      de suas capacidades.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    pricing_strategist = Agent(
        role="Especialista em Estratégias de Preço",
        goal=f"""Analisar as estratégias de precificação de {product_name}, comparando com produtos concorrentes 
                 e avaliando a relação custo-benefício.""",
        backstory=f"""Especialista em precificação e estratégias de mercado, com experiência em analisar modelos de precificação 
                      e identificar oportunidades de otimização.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    product_marketing_specialist = Agent(
        role="Especialista em Marketing de Produto",
        goal=f"""Desenvolver estratégias de marketing para {product_name}, focando em destacar seus benefícios e 
                 diferenciais no mercado.""",
        backstory=f"""Com profundo conhecimento em marketing de produtos, este especialista é capaz de criar campanhas 
                      eficazes que aumentam a visibilidade e a demanda para {product_name}.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    product_comparison_analyst = Agent(
        role="Analista de Comparação de Produtos",
        goal=f"""Comparar {product_name} com produtos concorrentes, destacando seus pontos fortes e fracos.""",
        backstory=f"""Especialista em análise comparativa, este agente avalia a competitividade de {product_name} 
                      em relação a outros produtos do mercado.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Coletar informações detalhadas sobre as especificações técnicas de {product_name}. 
                        Escrever um relatório com 10 tópicos, abordando os principais componentes, materiais, 
                        tecnologias e desempenho.""",
        expected_output="Relatório de especificações técnicas.",
        agent=product_specification_expert
    )

    task2 = Task(
        description=f"""Analisar a estratégia de preços de {product_name} em comparação com concorrentes. 
                        Incluir uma análise de preço vs. valor percebido e estratégias de precificação.""",
        expected_output="Relatório sobre estratégia de preços e comparação de valor.",
        agent=pricing_strategist
    )

    task3 = Task(
        description=f"""Desenvolver um plano de marketing para {product_name}, focado em destacar seus 
                        diferenciais no mercado.""",
        expected_output="Plano de marketing detalhado para o produto.",
        agent=product_marketing_specialist
    )

    task4 = Task(
        description=f"""Comparar {product_name} com outros produtos similares no mercado, destacando 
                        seus principais pontos fortes e fracos.""",
        expected_output="Análise comparativa de produtos.",
        agent=product_comparison_analyst
    )

    # Criar e Executar a Equipe
    product_detail_crew = Crew(
        agents=[product_specification_expert, pricing_strategist, product_marketing_specialist, product_comparison_analyst],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = product_detail_crew.kickoff()
    return crew_result


def create_product_differentiation_team(product_name, llm):

    max_iter = 25

    # Definir Agentes
    unique_selling_point_expert = Agent(
        role="Especialista em Proposta Única de Valor",
        goal=f"""Identificar e analisar os diferenciais exclusivos de {product_name}, destacando os principais pontos que 
                 o tornam único no mercado.""",
        backstory=f"""Especialista em identificar propostas únicas de valor, este agente se foca em entender o que diferencia 
                      {product_name} dos concorrentes, enfatizando características que atraem os consumidores.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    customer_perception_analyst = Agent(
        role="Analista de Percepção do Cliente",
        goal=f"""Analisar como os clientes percebem os diferenciais de {product_name} e como esses diferenciais influenciam 
                 suas decisões de compra.""",
        backstory=f"""Especialista em percepção do cliente, com foco em entender como os consumidores valorizam os diferenciais 
                      de {product_name} e como isso afeta sua escolha entre produtos concorrentes.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    competitive_edge_specialist = Agent(
        role="Especialista em Vantagem Competitiva",
        goal=f"""Avaliar como os diferenciais de {product_name} proporcionam uma vantagem competitiva em relação aos concorrentes, 
                 e como essa vantagem pode ser explorada.""",
        backstory=f"""Com ampla experiência em análise competitiva, este agente foca em como os diferenciais de {product_name} 
                      podem ser utilizados para conquistar uma posição de destaque no mercado.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    market_positioning_expert = Agent(
        role="Especialista em Posicionamento de Mercado",
        goal=f"""Desenvolver um plano de posicionamento de mercado para {product_name}, enfatizando seus diferenciais e como 
                 eles devem ser comunicados ao público-alvo.""",
        backstory=f"""Especialista em posicionamento de mercado, com experiência em criar estratégias para destacar os diferenciais 
                      de um produto e maximizar sua visibilidade e apelo no mercado.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Identificar e descrever os principais diferenciais de {product_name}. O relatório deve cobrir:
                        1. Características únicas do produto
                        2. Benefícios exclusivos para o consumidor
                        3. Comparação com produtos concorrentes
                        4. Inovação e tecnologia envolvida
                        5. Valor agregado ao cliente""",
        expected_output="Relatório detalhado sobre os diferenciais do produto.",
        agent=unique_selling_point_expert
    )

    task2 = Task(
        description=f"""Analisar como os clientes percebem os diferenciais de {product_name}. O relatório deve abordar:
                        1. Feedback e opiniões dos clientes
                        2. Percepções sobre as características exclusivas
                        3. Impacto na decisão de compra
                        4. Comparação com a percepção de concorrentes""",
        expected_output="Relatório sobre percepção do cliente e impacto dos diferenciais.",
        agent=customer_perception_analyst
    )

    task3 = Task(
        description=f"""Avaliar a vantagem competitiva proporcionada pelos diferenciais de {product_name}. O relatório deve incluir:
                        1. Análise de como os diferenciais oferecem uma vantagem competitiva
                        2. Estratégias para explorar essa vantagem
                        3. Comparação com a posição de mercado dos concorrentes
                        4. Oportunidades para maximizar a vantagem competitiva""",
        expected_output="Relatório sobre a vantagem competitiva e estratégias associadas.",
        agent=competitive_edge_specialist
    )

    task4 = Task(
        description=f"""Desenvolver um plano de posicionamento de mercado para {product_name}. O plano deve incluir:
                        1. Estratégias para comunicar os diferenciais ao público-alvo
                        2. Táticas para destacar os pontos fortes do produto
                        3. Sugestões de campanhas de marketing
                        4. Análise de posicionamento em relação aos concorrentes""",
        expected_output="Plano de posicionamento de mercado detalhado.",
        agent=market_positioning_expert
    )

    # Criar e Executar a Equipe
    product_differentiation_crew = Crew(
        agents=[unique_selling_point_expert, customer_perception_analyst, competitive_edge_specialist, market_positioning_expert],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = product_differentiation_crew.kickoff()
    return crew_result



def create_and_execute_related_products_research_team(product_name, llm):
    max_iter = 50

    # Definir Agentes
    interest_correlation_analyst = Agent(
        role="Analista de Correlação de Interesse",
        goal=f"""Identificar quais outros produtos estão correlacionados com o {product_name} com base no comportamento de compra dos clientes. 
                 O objetivo é descobrir produtos adicionais de interesse relacionado.""",
        backstory=f"""Especialista em correlacionar produtos com base em dados de comportamento de compra. 
                      Experiente em identificar produtos complementares e alternativas que atraem o mesmo público.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    customer_purchase_pattern_analyst = Agent(
        role="Analista de Padrões de Compra dos Clientes",
        goal=f"""Examinar padrões de compra para descobrir quais produtos são frequentemente comprados junto com o {product_name} 
                 ou como alternativas pelos clientes.""",
        backstory=f"""Especialista em analisar padrões de compra e comportamento do cliente. 
                      Hábil em identificar produtos frequentemente adquiridos em conjunto ou substitutos relevantes.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    market_trends_researcher = Agent(
        role="Pesquisador de Tendências de Mercado",
        goal=f"""Analisar tendências de mercado para identificar produtos relacionados que estão em alta ou ganhando popularidade 
                 entre os consumidores interessados no {product_name}.""",
        backstory=f"""Pesquisador com experiência em identificar e analisar tendências de mercado. 
                      Capaz de prever quais produtos relacionados estão emergindo e quais estão em alta.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    competitor_product_specialist = Agent(
        role="Especialista em Produtos Concorrentes",
        goal=f"""Identificar produtos similares ou alternativas oferecidas por concorrentes do {product_name}. 
                 O objetivo é entender quais produtos competem diretamente e quais são as alternativas mais relevantes.""",
        backstory=f"""Especialista em análise de produtos concorrentes. 
                      Hábil em comparar e identificar produtos similares oferecidos por concorrentes e suas estratégias de mercado.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    customer_feedback_analyst = Agent(
        role="Analista de Feedback dos Clientes",
        goal=f"""Coletar e avaliar feedback dos clientes para identificar produtos adicionais que eles expressaram interesse 
                 além do {product_name}. O objetivo é entender preferências e sugestões dos clientes.""",
        backstory=f"""Analista especializado em coletar e interpretar feedback dos clientes. 
                      Capaz de identificar padrões de interesse e sugestões para produtos relacionados.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Identificar quais outros produtos estão correlacionados com o {product_name} com base no comportamento de compra dos clientes. 
                        O relatório deve incluir produtos complementares e alternativas relevantes. 
                        O mês atual é Jan 2024.""",
        expected_output="Relatório detalhado sobre produtos correlacionados e de interesse relacionado.",
        agent=interest_correlation_analyst,
    )

    task2 = Task(
        description=f"""Analisar padrões de compra para descobrir quais produtos são frequentemente comprados junto com o {product_name} 
                        ou como alternativas. O relatório deve incluir insights sobre produtos complementares e substitutos. 
                        O mês atual é Jan 2024.""",
        expected_output="Relatório sobre padrões de compra e produtos frequentemente adquiridos em conjunto ou substitutos.",
        agent=customer_purchase_pattern_analyst,
    )

    task3 = Task(
        description=f"""Analisar tendências de mercado para identificar produtos relacionados que estão ganhando popularidade 
                        entre os consumidores interessados no {product_name}. O relatório deve incluir produtos emergentes e em alta. 
                        O mês atual é Jan 2024.""",
        expected_output="Relatório sobre tendências de mercado e produtos relacionados em alta.",
        agent=market_trends_researcher,
    )

    task4 = Task(
        description=f"""Identificar produtos similares ou alternativas oferecidas por concorrentes do {product_name}. 
                        O relatório deve incluir uma análise comparativa de produtos concorrentes e suas estratégias de mercado. 
                        O mês atual é Jan 2024.""",
        expected_output="Relatório sobre produtos concorrentes e suas alternativas relevantes.",
        agent=competitor_product_specialist,
    )

    task5 = Task(
        description=f"""Coletar e avaliar feedback dos clientes para identificar produtos adicionais que eles expressaram interesse 
                        além do {product_name}. O relatório deve incluir sugestões e preferências dos clientes. 
                        O mês atual é Jan 2024.""",
        expected_output="Relatório sobre feedback dos clientes e produtos de interesse adicional.",
        agent=customer_feedback_analyst,
    )

    # Criar e Executar a Equipe
    related_products_research_crew = Crew(
        agents=[interest_correlation_analyst, customer_purchase_pattern_analyst, market_trends_researcher, competitor_product_specialist, customer_feedback_analyst],
        tasks=[task1, task2, task3, task4, task5],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = related_products_research_crew.kickoff()
    return crew_result
