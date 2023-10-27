import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Cadastro de Contas")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: AbrirContaUI.listar()
    with tab2: AbrirContaUI.inserir()
    with tab3: AbrirContaUI.atualizar()
    with tab4: AbrirContaUI.excluir()

  def listar():
    contas = View.conta_listar()
    if len(contas) == 0:
      st.write("Nenhum conta cadastrado")
    else:
      dic = []
      for obj in contas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      if View.conta_inserir(nome, email, senha):
        st.success("Conta inserido com sucesso")
        time.sleep(2)
        st.rerun()
      else:
        st.error("E-mail já cadastrado")

  def atualizar():
    contas = View.conta_listar()
    if len(contas) == 0:
      st.write("Nenhum conta cadastrado")
    else:
      op = st.selectbox("Atualização de Contas", contas)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        id = op.get_id()
        if View.conta_atualizar(id, nome, email, senha):
          st.success("Conta atualizada com sucesso")
          time.sleep(2)
          st.rerun()
        else:
          st.error("E-mail já cadastrado para outra conta")

  def excluir():
    contas = View.conta_listar()
    if len(contas) == 0:
      st.write("Nenhuma conta cadastrado")
    else:
      op = st.selectbox("Exclusão de Contas", contas)
      if st.button("Excluir"):
        id = op.get_id()
        View.conta_excluir(id)
        st.success("Conta excluída com sucesso")
        time.sleep(2)
        st.rerun()