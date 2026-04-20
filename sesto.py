def fattoriale(num):
    risultato = 1
    for i in range(num, 0, -1):
        print("Passo:", risultato, "x", i, "=", risultato * i)
        risultato = risultato * i
    return risultato

numero = int(input("Di quale numero vuoi il fattoriale? "))
print("Risultato finale:", fattoriale(numero))