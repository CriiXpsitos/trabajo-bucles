num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero que sea mayor al numero anterior: "))

if num1 < num2:
    print(f"Los numeros que va desde {num1} hasta {num2} son:")
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("Como te lo dije el numero 1 debe ser mayor al 2")