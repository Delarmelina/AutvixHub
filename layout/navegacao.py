from msilib.schema import Icon
import streamlit as st

def Page(page):
    st.session_state.page = page

def Nav():

    st.sidebar.image('./assets/logovertical.png')

    st.sidebar.empty()
    BtHome = st.sidebar.button("Dashboard")
    BtProjetos = st.sidebar.button("Projetos")
    BtRelatorios = st.sidebar.button("Relatórios")
    BtColaboradores = st.sidebar.button("Colaboradores")

    if (BtHome):
        Page("Main")
    if (BtRelatorios):
        Page("Relatorios")
    if (BtProjetos):
        Page("Projetos")
    if (BtColaboradores):
        Page("Colaboradores")