cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))

contadorEstudiantes = 0
nota_maxima = float('-inf')
nota_minima = float('inf')
suma_notas = 0

while contadorEstudiantes < cantidadEstudiantes:
    contadorEstudiantes += 1
    print("Estudiante", contadorEstudiantes)
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    suma_notas_estudiante = nota1 + nota2 + nota3
    promedio_estudiante = suma_notas_estudiante / 3

    suma_notas += suma_notas_estudiante
    nota_maxima = max(nota_maxima, nota1, nota2, nota3)
    nota_minima = min(nota_minima, nota1, nota2, nota3)

promedio = suma_notas / (cantidadEstudiantes * 3)

print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
print("Promedio de notas:", promedio)
