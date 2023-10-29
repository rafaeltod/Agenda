import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Cadastro de Contas")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Cadastrar"):
      if View.conta_inserir(nome, email, senha):
        st.success("Conta inserido com sucesso")
        time.sleep(2)
        st.rerun()
      else:
        st.error("E-mail já cadastrado")