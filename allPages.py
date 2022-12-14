import streamlit as st

# Relatorios
from pages.Principais import relatorios
from pages.RH import RH

#Colaboradores
from pages.Principais import colaboradores

# Projetos
from pages.Principais import projetos

def Pages():

    # Inicialização do State
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Main'

    # --------------------------------------------------------------------
    # Pagina Inicial
    if ('Main' in st.session_state.page):
        st.text("Pagina Principal")

    # --------------------------------------------------------------------
    # Projetos
    if (st.session_state.page == 'Projetos'):
        projetos.Projetos()

    # --------------------------------------------------------------------
    # Relatórios
    if (st.session_state.page == 'Relatorios RH'):
        RH.RH()

    if (st.session_state.page == 'Relatorios'):
        relatorios.Pages()

    # --------------------------------------------------------------------
    # Colaboradores
    if (st.session_state.page == 'Colaboradores'):
        colaboradores.Colaboradores()
