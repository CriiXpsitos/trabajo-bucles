numeros = int(input("Digite un numero aquí: "))
acumuladorNumeros = 0

for i in range(0, numeros + 1, 2):
    acumuladorNumeros += i

print(f"El resultado de la suma de los numeros pares de {numeros} es {acumuladorNumeros}")