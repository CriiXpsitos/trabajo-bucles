numeros = int(input("ingrese un numero: "))
suma = 0
pares = 0
contador = 0

while contador <= numeros:
    if contador % 2 == 0:
        suma += contador
        pares += 1
    contador += 1

print(f"Los numeros pares estan dentro del numero {numeros} son: {pares}")
print(f"La suma de los numeros pares estanS dentro del numero {numeros} es: {suma}")