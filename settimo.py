persona = {
    "nome": "Mario",
    "eta": 30,
    "citta": "Milano"
}

# modifica un valore
persona["eta"] = 31

# aggiungi una nuova chiave
persona["lavoro"] = "programmatore"

print(persona)

for chiave, valore in persona.items():
    print(chiave, ":", valore)