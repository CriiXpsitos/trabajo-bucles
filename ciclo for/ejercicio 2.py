numero = int(input("ingresa tu numero: "))

if numero > 10: 
    acumuladorNumeros = 1 
    for i in range(1, 11):
        acumuladorNumeros *=i
    print(f"la multiplicacion de los primeros 10 numeros de {numero} es: {acumuladorNumeros}")
else: 
    acumuladorNumeros = 0 
    for a in range(0, numero):
        acumuladorNumeros += a
    print(f"el resultado es: {acumuladorNumeros}")