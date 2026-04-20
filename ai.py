from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

messaggi = []

while True:
    domanda = input("Tu: ")
    messaggi.append({"role": "user", "content": domanda})
    
    risposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messaggi
    )
    
    testo = risposta.choices[0].message.content
    messaggi.append({"role": "assistant", "content": testo})
    print("AI:", testo)