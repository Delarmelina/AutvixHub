import streamlit as st

from service.DBservice import obterUsuarios

def Colaboradores():

    st.title("Colaboradores")

    st.dataframe(obterUsuarios(), 5000)