import streamlit as st

def Pages():

    st.title("Relatórios")

    BtRH = st.button("Relatório de Horas")
    BtRDV = st.button("Relatório de Viagens")
    BtDenuncias = st.button("Denúncias")

    if (BtRH):
        st.session_state.page = "Relatorios RH"
        st.experimental_rerun()
    if (BtRDV):
        st.session_state.page = "Relatorios RDV"
        st.experimental_rerun()
    if (BtDenuncias):
        st.session_state.page = "Relatorios Denuncias"
        st.experimental_rerun()
