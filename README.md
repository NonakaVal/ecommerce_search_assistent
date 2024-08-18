
# Ferramentas de Pesquisa de Mercado com IA

## Descrição

Esta aplicação é uma ferramenta desenvolvida para analisar o mercado e criar estratégias de negócios utilizando modelos avançados de inteligência artificial. Através de uma interface Streamlit, os usuários podem fornecer o nome de um produto e obter análises detalhadas sobre demanda, comportamento do consumidor, concorrência, tendências, feedback de clientes e muito mais.

<img src="https://i.imgur.com/yTozdF5.png" alt="Exemplo imagem" width="90%" >
<img src="https://i.imgur.com/B3baiJq.png" alt="Exemplo imagem" width="90%" >

---


### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [ ] Optimizar Prompts das Equipes
- [ ] Melhorar as query de Pesquisa

---

## 💻 Pré-requisitos

- [**Python**](https://www.python.org/downloads/) - Linguagem principal para o desenvolvimento da aplicação.
- [**Streamlit**](https://streamlit.io/) - Framework para criar a interface web interativa.
- [**CrewAI**](https://www.crewai.com/) - Framework para criar suas multiagentes especializados.
- [**LangChain**](https://www.langchain.com/) - Biblioteca para integração com modelos de linguagem.
- [**dotenv**](https://pypi.org/project/python-dotenv/) - Gerencia variáveis de ambiente.

### Chaves de API necessárias.

- [**OpenAI**](https://platform.openai.com) - Modelo de linguagem utilizado para gerar insights e análises.
- [**Serper**](https://serper.dev/) - API para realizar buscas na web e obter resultados relevantes para análises e pesquisas.
- [**Browserless**](https://www.browserless.io/) - Serviço para scraping de dados.

---

## 🚀  Começando

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/NonakaVal/new_mkt_research_tools.git
   ```

2. **Crie um Ambiente Virtual**

   ```bash
   python -m venv venv_name
   source venv_name/bin/activate  # No Windows: venv_name\Scripts\activate
   ```

3. **Instale as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Chaves da API**

   Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

   ```text
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   SERPER_API_KEY=YOUR_SERPER_API_KEY
   BROWSERLESS_API_KEY=YOUR_BROWSERLESS_API_KEY
   ```

---   

## ☕ Usando

1. **Executar a Aplicação**

   Para iniciar a aplicação, execute o seguinte comando:

   ```bash
   streamlit run main.py
   ```

   ou

   ```bash
   python -m streamlit run main.py
   ```

2. **Interação com a Aplicação**

   - **Digite o Nome do Produto**: Insira o nome do produto que deseja analisar no campo de entrada.
   - **Execute a Pesquisa**: Clique no botão "Executar Pesquisa" para iniciar a análise.
   - **Visualize os Resultados**: Acompanhe o processamento e visualize os resultados detalhados nos expansores de informação.

---

## 📫 Contribuindo para este projeto.

Para contribuir com <nome_do_projeto>, siga estas etapas:

1. Fork este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

---


---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. 





