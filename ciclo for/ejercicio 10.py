numero = int(input("Ingrese algun numero mayor que sea 0: "))

if numero > 0:
    for i in range(1,numero + 1): 
        if numero % i == 0:
            print(f"{i} es divisor de {numero}")
else:
    print(" le dije que el numero debe ser mayor a 0... *cara enojada*")