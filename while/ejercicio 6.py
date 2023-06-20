contadorNotas = 0
sumaNotas = 0
nota = 0

while nota != -1:
    nota = float(input("Ingrese una nota: "))
    if nota != -1:
        sumaNotas += nota
        contadorNotas += 1

promedio = sumaNotas / contadorNotas

print("El promedio de las notas ingresadas es:", promedio)
