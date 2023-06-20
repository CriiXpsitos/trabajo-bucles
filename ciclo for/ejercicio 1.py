numero = int(input("ingresa el numero de elementos que quieres sumar"))
suma = 0 

for i in range (1, numero+1):
    suma += i

print(f"la suma de los {numero} primeros numero es: {suma}")
