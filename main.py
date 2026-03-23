import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# carregar variáveis do .env
load_dotenv()

# pegar chave com segurança
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.write("### ChatBot com IA")

# memória do chat
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# mostrar histórico
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# input do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # exibir mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)

    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": mensagem_usuario
    })

    # resposta da IA
    resposta_modelo = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["lista_mensagens"]
    )

    resposta_ia = resposta_modelo.choices[0].message.content

    # mostrar resposta
    st.chat_message("assistant").write(resposta_ia)

    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": resposta_ia
    })