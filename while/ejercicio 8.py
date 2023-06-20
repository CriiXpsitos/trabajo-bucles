numero = int(input("Ingrese un número entero mayor que cero: "))

while numero <= 0:
    numero = int(input("Número inválido. Ingrese un número entero mayor que cero: "))

print("Divisores de", numero, ":")

divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1
