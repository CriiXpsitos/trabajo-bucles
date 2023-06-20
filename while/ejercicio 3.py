numero = int(input("Ingrese un numero: "))
contador = 0
suma = 0

print(f"Los numeros impares que hay en {numero} son:")
while contador != numero+1:
    if contador % 2 != 0:
        suma += contador 
        print(contador)
    contador += 1
print(f"La suma de los numeros impares que hay de {numero} es: {suma}")