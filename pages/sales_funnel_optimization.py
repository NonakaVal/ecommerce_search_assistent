import os
import sys
import time
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crews.Sales_Funnel_Optimization import create_sales_funnel_optimization_team
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
                crew_result = create_sales_funnel_optimization_team(product_name=product_name, llm=llm)
        # Parar o cronômetro
        end_time = time.time()
        total_time = end_time - start_time
        stopwatch_placeholder.text(f"Tempo Total Decorrido: {total_time:.2f} segundos")

if __name__ == "__main__":
    run_crewai_app()
