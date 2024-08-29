#El gerente de ventas de Mercado Libre desea habilitar Envíos Gratis para compras a partir de los 15.000
#pesos. Se necesita un programa que ingrese el monto de la compra, e informe al usuario si accede o no al
#beneficio.

precio= int (input("Ingrese Monto "))
if precio >= 15000:
    print ("Tiene envio gratis")
else:
    print ("No tiene envio gratis")