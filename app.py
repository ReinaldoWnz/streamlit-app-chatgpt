import streamlit as st
import requests

st.title("Assistente de Roteiros 🎬 - Groq")

prompt = st.text_area("Digite o tema do vídeo:", "")

if st.button("Gerar roteiro") and prompt:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}"
    }
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    roteiro = result["choices"][0]["message"]["content"]
    st.subheader("📑 Roteiro Gerado")
    st.write(roteiro)
