nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))

if eta < 18:
    print("Ciao", nome + "! Sei minorenne.")
elif eta < 65:
    print("Ciao", nome + "! Sei adulto.")
else:
    print("Ciao", nome + "! Sei in pensione o sei Actarus.")