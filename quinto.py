def tabellina(num):
    for i in range(1, 11):
        print(i, "x", num, "=", i * num)

numero = int(input("Di quale numero vuoi la tabellina? "))
tabellina(numero)