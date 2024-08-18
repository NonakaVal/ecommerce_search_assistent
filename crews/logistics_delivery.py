from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools


def create_logistics_delivery_team(product_name, llm):

    max_iter = 50

    # Definir Agentes
    logistics_efficiency_expert = Agent(
        role="Especialista em Eficiência Logística",
        goal=f"""Analisar a eficiência das operações de entrega para {product_name}, identificando áreas de melhoria e propondo soluções para otimizar o processo.""",
        backstory=f"""Especialista em logística com experiência em otimização de operações de entrega. Capaz de avaliar processos logísticos e propor melhorias para aumentar a eficiência e reduzir custos.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    delivery_process_analyst = Agent(
        role="Analista de Processos de Entrega",
        goal=f"""Avaliar e mapear os processos de entrega para {product_name}, identificando gargalos e ineficiências. Propor melhorias baseadas em análise detalhada dos processos atuais.""",
        backstory=f"""Com experiência em análise e mapeamento de processos logísticos, este analista avalia a eficiência das entregas e sugere melhorias para otimizar o processo para {product_name}.""",
        verbose=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        allow_delegation=True,
        llm=llm,
        max_iter=max_iter
    )

    customer_satisfaction_specialist = Agent(
        role="Especialista em Satisfação do Cliente",
        goal=f"""Coletar e analisar feedback dos clientes sobre as operações de entrega de {product_name} para entender o impacto na satisfação do cliente e identificar áreas de melhoria.""",
        backstory=f"""Especialista em analisar feedbacks de clientes sobre serviços de entrega, focado em identificar pontos de insatisfação e propor melhorias para aumentar a satisfação com as entregas.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    logistics_strategy_developer = Agent(
        role="Desenvolvedor de Estratégias Logísticas",
        goal=f"""Desenvolver e implementar estratégias para melhorar a eficiência das operações de entrega para {product_name}, com base nas análises e feedbacks recebidos.""",
        backstory=f"""Especialista em criar e aplicar estratégias logísticas para otimizar processos de entrega, visando aumentar a eficiência e reduzir custos, com foco específico em {product_name}.""",
        verbose=True,
        allow_delegation=True,
        tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website, ScrapeWebsiteTool(), WebsiteSearchTool()],
        llm=llm,
        max_iter=max_iter
    )

    # Definir Tarefas
    task1 = Task(
        description=f"""Analisar a eficiência das operações de entrega para {product_name}. O relatório deve incluir:
                        1. Análise de tempos de entrega
                        2. Identificação de gargalos e ineficiências
                        3. Comparação com benchmarks de mercado
                        4. Sugestões de melhoria para o processo de entrega
                        5. Impacto das operações na satisfação do cliente""",
        expected_output="Relatório detalhado sobre a eficiência das operações de entrega e áreas de melhoria.",
        agent=logistics_efficiency_expert,
    )

    task2 = Task(
        description=f"""Avaliar e mapear os processos de entrega para {product_name}, identificando pontos críticos e oportunidades de otimização. O relatório deve abordar:
                        1. Mapeamento detalhado dos processos de entrega
                        2. Análise de gargalos e ineficiências
                        3. Recomendações para otimização
                        4. Medidas para melhorar a eficiência operacional""",
        expected_output="Relatório sobre processos de entrega e sugestões para otimização.",
        agent=delivery_process_analyst,
    )

    task3 = Task(
        description=f"""Coletar e analisar feedback de clientes sobre as operações de entrega de {product_name}. O relatório deve incluir:
                        1. Principais pontos de feedback positivo e negativo
                        2. Impacto do feedback na satisfação do cliente
                        3. Identificação de áreas críticas de insatisfação
                        4. Sugestões para melhorar a experiência de entrega""",
        expected_output="Relatório sobre feedback de clientes e recomendações para melhorar a satisfação.",
        agent=customer_satisfaction_specialist,
    )

    task4 = Task(
        description=f"""Desenvolver estratégias para melhorar a eficiência das operações de entrega de {product_name}. O plano deve incluir:
                        1. Estratégias para otimizar o processo de entrega
                        2. Implementação de melhorias com base em análises e feedbacks
                        3. Planos de ação para resolver gargalos identificados
                        4. Monitoramento e ajustes contínuos""",
        expected_output="Plano estratégico para melhorar a eficiência das operações de entrega.",
        agent=logistics_strategy_developer,
        context=[task1, task2, task3]
    )

    # Criar e Executar a Equipe
    logistics_delivery_crew = Crew(
        agents=[logistics_efficiency_expert, delivery_process_analyst, customer_satisfaction_specialist, logistics_strategy_developer],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        manager_llm=llm
    )

    crew_result = logistics_delivery_crew.kickoff()
    return crew_result
