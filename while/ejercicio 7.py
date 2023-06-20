end = 0
suma = 0

while not end:
    numeros = int(input("ponga todos los numeros que... ojo que sean ENTEROS del teclado: "))
    suma += numeros
    if numeros == end:
        print(f"La suma de los numeros del teclado ingresados es {suma}")
        break