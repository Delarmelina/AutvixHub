import streamlit as st

from service.DBservice import getProjetos

def Projetos():

    st.title("Projetos")


    teste = getProjetos()

    st.dataframe(teste, 5000)