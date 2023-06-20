notas1 = int(input("ingrese las notas para sacar el promedio: "))
acumulador = 0

for i in range(1, notas1 + 1):
    print(f"ingrese las {i} notas:", end=" ")
    nota = int(input())
    acumulador += nota
    promedio = acumulador / notas1

print(f"El promedio de sus notas es {promedio}")