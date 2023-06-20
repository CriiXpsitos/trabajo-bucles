montoFactura = 1
totalPagar = 0

while monto_factura != 0:
    monto_factura = float(input("Ingrese el numero de la factura: "))
    totalPagar += montoFactura

if totalPagar > 1000:
    descuento = totalPagar * 0.1
    totalPagar -= descuento

print("Total a pagar: $", totalPagar)
