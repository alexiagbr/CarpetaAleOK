'''Escribir un programa que cree un diccionario
simulando una cesta de la compra. El programa debe preguntar el articulo y su precio
y añadir el par al diccionario, hasta que el usuario decida terminar.
Despues se debe mostrar por pantalla la lista de la compra y el coste total, 
con el siguiente formato'''

cesta = {}
continuar = True
while continuar:
    producto = input('Introduce un articulo: ') #ingresar el articulo clave
    precio = float(input('Introduce el precio de ' + producto + ': ')) #precio del articulo
    cesta[producto] = precio #agrego al diccionario clave y los valores
    pregunta = input('¿Quieres añadir articulos a la lista (Si/No)?')
    if pregunta == 'NO':
        continuar = False

    print(cesta)

    coste = 0
    print('Lista de la compra')
    for producto, precio, in cesta.items():
        print(f'{producto}: {precio}') #sintaxis oara mostrar por pantalla un objeto en orden
        coste += precio
    print('Coste total: ', coste)