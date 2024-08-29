#ejercicio de la farmacia

Pedido1= int(input("Ingrese la cantidad solicitada para la primera sucursal"))
Pedido2= int(input("Ingrese la cantidad solicitada para la segunda sucursal"))
Pedido3= int(input("Ingrese la cantidad solicitada para la tercera sucursal"))

if Pedido1>=100:
    print("el pedido de la primera sucursal es gratis")
else:
    print("no posee envio gratis.")
if Pedido2>=100:
         print("el pedido de la segunda sucursal es gratis")
else:
         print("no posee envio gratis.")
if Pedido3>=100:
             print("el pedido de la Tercera sucursal es gratis")
else:
             print("no posee envio gratis.")
             
print("EL total de pedidos es de",(Pedido1+Pedido2+Pedido3))