import streamlit as st

st.set_page_config(
     page_title='Market Research App',
     layout="wide",
     initial_sidebar_state="expanded",
)

LOGO_URL_LARGE = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
LOGO_URL_SMALL = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
st.logo(
    LOGO_URL_LARGE,
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)

st.markdown("""
## Assistentes de Pesquisa 🔍

Olá, sou [Valdenir Nonaka](https://linktr.ee/NonakaVal) 👋, um estudante de Ciência da Computação especializado em Ciência de Dados.

Atualmente, estou trabalhando em uma **ferramenta de pesquisa** desenvolvida com [CrewAI](https://www.crewai.com/) e tecnologia da [OpenAI](https://platform.openai.com).


Estou testanto diversas configurações de equipes e prompts, cada página recebe sua própria crew.
            
Você pode gerenciar e configurar as equipes no diretório `crews/` do projeto.


Altere entre `StreamToExpander` ou `StreamToExpander_detailed` para receber todas as saídas ou só os resultados.

            
                    
""")



st.divider()


st.markdown(
            """


<img src="https://i.imgur.com/vvGvjPp.jpg" alt="Image" width="50%" style="display: block; ">


""", unsafe_allow_html =True
            )

st.divider()

st.link_button("Meu portifólio com outros projetos..", "https://nonaka-portfolio-kfhauom.gamma.site/")


st.markdown(
            """
<p align="left">
  💌 Minhas Redes: ⤵️
</p>

<p align="left">
  <a href="mailto:valdenirnonaka@gmail.com" title="Gmail">
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=LINK-DO-SEU-GMAIL" alt="Gmail"/></a>
  <a href="https://www.linkedin.com/in/valdenir-nonaka-5433712a8/" title="LinkedIn">
  <img src="https://img.shields.io/badge/-Linkedin-0e76a8?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN" alt="LinkedIn"/></a>
  <a href="https://api.whatsapp.com/send?phone=5515998304344" title="WhatsApp">
  <img src="https://img.shields.io/badge/-WhatsApp-25d366?style=flat-square&labelColor=25d366&logo=whatsapp&logoColor=white&link=API-DO-SEU-WHATSAPP" alt="WhatsApp"/></a>
  <a href="https://www.facebook.com/profile.php?id=61555190195313" title="Facebook">
  <img src="https://img.shields.io/badge/-Facebook-3b5998?style=flat-square&labelColor=3b5998&logo=facebook&logoColor=white&link=LINK-DO-SEU-FACEBOOK" alt="Facebook"/></a>
  <a href="https://www.instagram.com/nonaka.val/" title="Instagram">
  <img src="https://img.shields.io/badge/-Instagram-DF0174?style=flat-square&labelColor=DF0174&logo=instagram&logoColor=white&link=LINK-DO-SEU-INSTAGRAM" alt="Instagram"/></a>
  <a href="https://www.youtube.com/@nonaka96" title="Instagram">
  <img src="https://img.shields.io/badge/-youtube-ff0000?style=flat-square&labelColor=%20ff0000&logo=youtube&logoColor=white&link=LINK-DO-SEU-INSTAGRAM alt="Instagram"/></a>
</p>




""", unsafe_allow_html =True
            )








