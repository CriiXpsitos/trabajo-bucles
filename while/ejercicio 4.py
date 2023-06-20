numero1 = int(input("Ingrese su primer numero: "))
numero2 = int(input("Ingrese su segundo numero: "))
contador= numero1 - 1
numeros = 0

if numero1 < numero2:
    print(f"Los numeros que son del desde {numero1} hasta {numero2} son:")
    while contador != numero2:
        numeros += contador
        contador += 1
        print(contador)
else:
    print("Como le dije... el numero debe ser menor al segundo")