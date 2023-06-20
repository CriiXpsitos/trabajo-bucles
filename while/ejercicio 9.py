contadorTemperaturas = 0
sumaTemperaturas = 0
temperaturaMaxima = float('-inf')
temperaturaMinima = float('inf')
temperatura = float(input("Ingrese una temperatura (0 para finalizar): "))

while temperatura != 0:
    contadorTemperaturas += 1
    sumaTemperaturas += temperatura

    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura

    if temperatura < temperatura_minima:
        temperatura_minima = temperatura

    temperatura = float(input("Ingrese una temperatura (0 para finalizar): "))

if contadorTemperaturas > 0:
    temperaturaPromedio = sumaTemperaturas / contadorTemperaturas
    print("Temperatura más alta:", temperaturaMaxima)
    print("Temperatura más baja:", temperaturaMinima)
    print("Temperatura promedio:", temperaturaPromedio)
else:
    print("No se ingresaron temperaturas.")
