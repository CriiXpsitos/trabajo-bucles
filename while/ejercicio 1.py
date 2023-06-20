numero = int(input("ingrese un numero: "))
contador = 0

if numero > 10:
    acumulador = 1
    while contador != 10:
        contador += 1
        acumulador *= contador
    print(f"El resultado es: {acumulador}")

else:
    acumulador = 0
    while contador < numero:
        contador += 1
        acumulador += contador
    print(f"El resultado es: {acumulador}")

