cantidadTemperaturas = int(input("cuantas temperaturas usted va poner?     "))
temperaturas = []

for i in range(cantidadTemperaturas):
    temperatura = float(input("Ingrese la temperatura: "))
    temperaturas += [temperatura]

temperaturaMaxima = max(temperaturas)
temperaturaMinima = min(temperaturas)
temperaturaPromedio = sum(temperaturas) / len(temperaturas)

print("Temperatura más alta:", temperaturaMaxima)
print("Temperatura más baja:", temperaturaMinima)
print("Temperatura promedio:", temperaturaPromedio)

