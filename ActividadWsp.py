'''Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'''

facturas = {} #diccionario vacio
cobrado=0
pendiente=0
def mostrar_factura():
    
    numero_factura = int (input("Ingrese el Nro de factura: ")) #clave del diccionario
    costo_factura = float (input("Ingrese el monto de la factura: ")) #valor o monto de la factura
    
    facturas[numero_factura] = costo_factura
    print(F"factura {numero_factura} añadida ")
    
def pagar_factura():
    numero_factura = int(input("Ingrese el numero de la factura a pagar "))
    if numero_factura in facturas:
        costo_pagado= facturas.pop(numero_factura)
        cobrado = cobrado+costo_pagado
        pendiente = pendiente-costo_pagado
        print(F"el monto pagado de la factura {numero_factura} por un monto {costo_pagado}")
        print(F"Cantidad cobrada de la factura: {cobrado}")
        print(F"Total pendiente a cobrar: {pendiente}")
    else:
        print (F"No existe la factura {numero_factura}")
        
def mostrar_factura():
    total_cobrado =sum(facturas.values())
    total_pendiente = sum(facturas.values()) - total_cobrado
    
    print(f"Cantidad cobrada de la factura: {total_cobrado}")
    print(F"Total pendiente a cobrar: {total_pendiente}")
            
    
        
    
    
    
    