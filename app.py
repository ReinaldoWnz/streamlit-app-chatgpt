import streamlit as st
from openai import OpenAI

# Inicializa cliente
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Assistente de Roteiros 🎬")

prompt = st.text_area("Digite seu tema de vídeo:")
if st.button("Gerar roteiro"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    st.write(response.choices[0].message.content)
