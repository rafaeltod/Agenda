import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Cadastro de Conta no Sistema")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Cadastrar"):
      if View.cliente_inserir(nome, email, fone, senha):
        st.success("Conta inserida com sucesso")
        time.sleep(2)
        st.rerun()
      else:
        st.error("E-mail já cadastrado")