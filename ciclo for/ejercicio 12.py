cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
nota_maxima = float('-inf')
nota_minima = float('inf')
suma_notas = 0

for i in range(cantidad_estudiantes):
    print("Estudiante", i+1)
    suma_estudiante = 0
    for j in range(4):
        nota = float(input("Ingrese la nota {}: ".format(j+1)))
        suma_estudiante += nota
        nota_maxima = max(nota_maxima, nota)
        nota_minima = min(nota_minima, nota)
    suma_notas += suma_estudiante

promedio = suma_notas / (cantidad_estudiantes * 4)

print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
print("Promedio de notas:", promedio)
