# Definimos las variables para los precios y el monto total
precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))
monto_total = 0.0

# Encontramos el precio del producto más barato
menor_precio = min(precio1, precio2, precio3)

# Calculamos el monto total con la promoción 3x2
if menor_precio == precio1:
    monto_total = precio2 + precio3
elif menor_precio == precio2:
    monto_total = precio1 + precio3
else:
    monto_total = precio1 + precio2

# Mostramos los resultados
print("El precio del producto más barato es:", menor_precio)
print("El monto total de la compra con la promoción 3x2 es:", monto_total)
