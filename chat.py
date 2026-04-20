from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.title("Il mio Chatbot 🤖")

if "messaggi" not in st.session_state:
    st.session_state.messaggi = []

for msg in st.session_state.messaggi:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

domanda = st.chat_input("Scrivi un messaggio...")

if domanda:
    st.session_state.messaggi.append({"role": "user", "content": domanda})
    
    risposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messaggi
    )
    
    testo = risposta.choices[0].message.content
    st.session_state.messaggi.append({"role": "assistant", "content": testo})
    st.rerun()