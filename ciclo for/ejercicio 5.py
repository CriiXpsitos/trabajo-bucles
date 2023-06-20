numero = int(input("Ingrese un número: "))
suma = 0
contador = 0

for i in range(1, numero+1):
    if i % 2 != 0:
        suma += i
        contador += 1

print(f"La suma de todos los números impares desde 1 hasta {numero} es: {suma}")
print(f"Hay {contador}números impares desde 1 hasta {numero}")
