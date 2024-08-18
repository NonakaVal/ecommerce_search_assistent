import os
import sys
import time
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crews.crewai_setup import create_crewai_setup
from tools.exp_config import StreamToExpander, StreamToExpander_detailed

# Load api key
load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')
openai_api_key = openai_key

# Configuração inicial do expander
expander_type = st.sidebar.radio(
    "Escolha o tipo saída",
    ["StreamToExpander", "StreamToExpander_detailed"]
)

if expander_type == "StreamToExpander":
    expdr_config = StreamToExpander(st)
else:
    expdr_config = StreamToExpander_detailed(st)

# # Descrições
# with st.expander("Sobre essa Crew..."):
#     st.markdown("""    
# **Agente 1: Analista de Pesquisa de Mercado**  
# - Objetivo: Analisar a demanda de mercado e sugerir estratégias de marketing.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre análise de demanda de mercado e estratégias de marketing.

# **Agente 2: Especialista em Comportamento do Consumidor**  
# - Objetivo: Analisar preferências e comportamentos de compra do público-alvo.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório detalhado sobre comportamento de compra dos consumidores.

# **Agente 3: Especialista em Análise de Concorrência**  
# - Objetivo: Avaliar a concorrência e identificar estratégias dos principais competidores.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre análise de concorrência e diferenciação no mercado.

# **Agente 4: Especialista em Análise de Tendências**  
# - Objetivo: Analisar tendências emergentes e impacto na demanda futura.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre tendências emergentes e seu impacto no mercado.

# **Agente 5: Analista de Feedback de Clientes**  
# - Objetivo: Coletar e analisar feedback de clientes sobre produtos similares.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre feedback de clientes e sugestões de melhorias.

# **Agente 6: Pesquisador de Dados Secundários**  
# - Objetivo: Recolher e analisar dados secundários relevantes.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre dados secundários e seu impacto na análise de demanda.

# **Agente 7: Planejador Estratégico**  
# - Objetivo: Desenvolver planos estratégicos detalhados baseados em análises da equipe.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Plano estratégico detalhado com recomendações práticas.

# **Agente 8: Avaliador de Impacto Estratégico**  
# - Objetivo: Avaliar o impacto das estratégias e tendências propostas no mercado.  
# - Ferramentas: Pesquisa na internet, scraping de sites e ferramentas de busca.  
# - Tarefas: Relatório sobre impacto das estratégias e recomendações de ajustes.
# """, unsafe_allow_html=True)

# Interface Streamlit
def run_crewai_app():
    if openai_api_key:
        try:
            # Criar uma instância do modelo ChatOpenAI
            llm = ChatOpenAI(
                model='gpt-3.5-turbo',
                api_key=openai_api_key
            )
            st.success("A chave da API do OpenAI está configurada e o LLM está pronto para usar!")    
        except Exception as e:
            st.error(f"Ocorreu um erro ao configurar o LLM: {e}")
    else:
        st.warning("Por favor, insira uma chave de API do OpenAI válida para continuar.")
    
    product_name = st.text_input("Digite o nome do produto para analisar o mercado e a estratégia de negócios.")
    
    if st.button("Executar Pesquisa"):
        stopwatch_placeholder = st.empty()
        
        # Iniciar o cronômetro
        start_time = time.time()
        with st.expander("Processando!"):
            sys.stdout = expdr_config
            with st.spinner("Gerando Resultados"):
                crew_result = create_crewai_setup(product_name=product_name, llm=llm)
        # Parar o cronômetro
        end_time = time.time()
        total_time = end_time - start_time
        stopwatch_placeholder.text(f"Tempo Total Decorrido: {total_time:.2f} segundos")

if __name__ == "__main__":
    run_crewai_app()
