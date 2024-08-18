from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

def create_sales_funnel_optimization_team(product_name, llm):

    max_iter = 25

    # Definir Agentes
    funnel_analysis_expert = Agent(
        role="Especialista em Análise do Funil de Vendas",
        goal=f"""Analisar o funil de vendas de {product_name} para identificar pontos de atrito e oportunidades de melhoria em cada etapa do processo de compra.""",
        backstory=f"""Especialista em funis de vendas com foco em entender e otimizar o processo de compra. Este agente irá examinar o desempenho de cada etapa do funil e recomendar melhorias.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    lead_generation_specialist = Agent(
        role="Especialista em Geração de Leads",
        goal=f"""Otimizar as estratégias de geração de leads para aumentar o número e a qualidade dos leads no funil de vendas de {product_name}.""",
        backstory=f"""Especialista em geração de leads, com experiência em desenvolver e implementar estratégias para atrair e qualificar leads, melhorando o início do funil de vendas.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    conversion_rate_expert = Agent(
        role="Especialista em Taxa de Conversão",
        goal=f"""Analisar e otimizar a taxa de conversão em cada etapa do funil de vendas de {product_name}, identificando e removendo obstáculos que impedem a conversão.""",
        backstory=f"""Especialista em taxas de conversão, focado em melhorar a eficácia do funil de vendas, aumentando a porcentagem de leads que se tornam clientes.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    customer_retention_specialist = Agent(
        role="Especialista em Retenção de Clientes",
        goal=f"""Desenvolver e implementar estratégias para melhorar a retenção de clientes após a conversão no funil de vendas de {product_name}.""",
        backstory=f"""Especialista em retenção de clientes, com experiência em criar e aplicar estratégias para manter os clientes engajados e satisfeitos, promovendo a lealdade e a repetição de compras.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Analisar o funil de vendas de {product_name} para identificar pontos críticos e áreas de melhoria. O relatório deve incluir:
                        1. Análise das taxas de conversão em cada etapa
                        2. Identificação de gargalos e pontos de atrito
                        3. Recomendações para otimização""",
        expected_output="Relatório de análise do funil de vendas e sugestões de melhorias.",
        agent=funnel_analysis_expert
    )

    task2 = Task(
        description=f"""Revisar e otimizar as estratégias de geração de leads para aumentar o volume e a qualidade dos leads. O relatório deve cobrir:
                        1. Estratégias atuais de geração de leads
                        2. Eficácia e desempenho das campanhas
                        3. Recomendações para melhorias e novos canais""",
        expected_output="Relatório sobre otimização da geração de leads.",
        agent=lead_generation_specialist
    )

    task3 = Task(
        description=f"""Analisar e melhorar a taxa de conversão em cada etapa do funil de vendas. O relatório deve incluir:
                        1. Taxas de conversão atuais e comparação com benchmarks
                        2. Identificação de obstáculos à conversão
                        3. Sugestões para melhorar a eficácia de conversão""",
        expected_output="Relatório de análise da taxa de conversão e recomendações de otimização.",
        agent=conversion_rate_expert
    )

    task4 = Task(
        description=f"""Desenvolver estratégias para melhorar a retenção de clientes após a conversão. O relatório deve incluir:
                        1. Análise das taxas de retenção e engajamento
                        2. Identificação de oportunidades para fidelização
                        3. Recomendações para melhorar a experiência do cliente e a retenção""",
        expected_output="Relatório sobre estratégias de retenção de clientes e suas implementações.",
        agent=customer_retention_specialist
    )

    # Criar e Executar a Equipe
    sales_funnel_crew = Crew(
        agents=[funnel_analysis_expert, lead_generation_specialist, conversion_rate_expert, customer_retention_specialist],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = sales_funnel_crew.kickoff()
    return crew_result
