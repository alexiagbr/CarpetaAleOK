"""Ejercicio 1: Filtrar Números Pares
Instrucciones:
Crea una lista de números del 1 al 20. Utiliza una función lambda y la 
función filter para obtener una nueva lista quecontenga solo los números pares.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_pares = list(filter (lambda x: x%2==0, lista))
print (lista_pares)"""


"""
Ejercicio 2: Mapear a Cuadrados
Instrucciones:
Dada una lista de números del 1 al 10, utiliza una función lambda y la función map para obtener una nueva lista con los
cuadrados de esos números.
"""

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lista_cuadrado = list(map (lambda x: x*x, lista))
#print(lista_cuadrado)

"""
Ejercicio 3: Sumar Listas de Elementos
Instrucciones:
Dadas dos listas de números del mismo tamaño, utiliza una función lambda y la función map para obtener una nueva lista
que contenga la suma de los elementos en las mismas posiciones de ambas listas.
"""
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista_suma = list(map (lambda x,y: x+y, lista1, lista2))
print(lista_suma)

"""
Ejercicio 4: Filtrar Palabras con más de 5 Letras
Instrucciones:
Dada una lista de palabras, utiliza una función lambda y la función filter para obtener una nueva lista que contenga
solo las palabras con más de 5 letras.
"""
#lista = ["tomate", "cebolla", "pizza", "auto", "caramelo" ]
#print(lista)
#lista_letras = list(filter(lambda palabra : len(palabra) >5, lista))
#print(lista_letras)
