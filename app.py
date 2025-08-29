import streamlit as st
import google.generativeai as genai

# Configura a chave a partir dos secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🎬 Gerador de Roteiros com Gemini")

prompt = st.text_area("Escreva o tema do vídeo:", "")

if st.button("Gerar roteiro") and prompt:
    model = genai.GenerativeModel("gemini-1.5-flash")  # ou gemini-1.5-pro para mais qualidade
    response = model.generate_content(f"Crie um roteiro de vídeo em tópicos sobre: {prompt}")
    
    st.subheader("📑 Roteiro Gerado")
    st.write(response.text)
