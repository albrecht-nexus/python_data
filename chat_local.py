import streamlit as st
from ollama import Client

client = Client()

st.title("Il mio Chatbot 🤖 (locale)")

if "messaggi" not in st.session_state:
    st.session_state.messaggi = [
        {"role": "system", "content": """Sei un fratello maggiore esperto di programmazione Python e tecnologia. 
Rispondi sempre e solo in italiano.
Sei diretto e sincero: se l'utente sbaglia díglielo chiaramente e spiega perché.
Se non sai qualcosa o non sei sicuro dillo esplicitamente, senza inventare.
Niente convenevoli, niente frasi di circostanza. Vai dritto al punto.
Sei paziente e disponibile a spiegare le cose più volte in modi diversi, ma senza perdere tempo in complimenti inutili."""}
    ]

for msg in st.session_state.messaggi:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

domanda = st.chat_input("Scrivi un messaggio...")

if domanda:
    st.session_state.messaggi.append({"role": "user", "content": domanda})
    
    risposta = client.chat(
        model="llama3.1:latest",
        messages=st.session_state.messaggi
    )
    
    testo = risposta.message.content
    st.session_state.messaggi.append({"role": "assistant", "content": testo})
    st.rerun()