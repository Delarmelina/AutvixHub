import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Autvix Engenharia", layout="wide")

# Carregamento do CSS
import style.style as style
style.style()

# Navegação
import layout.navegacao as Nav
Nav.Nav()

# Todas as Paginas
from allPages import Pages
Pages()