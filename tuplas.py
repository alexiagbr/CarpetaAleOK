# las tuplas son como las listas pero con algunas diferencias

# primeras diferencias

lista = ["Python", "JavaScript", "C," "C++"] #las listas van con corchete

tupla = ("Python", "JavaScript", "C," "C++") #las tuplas van con parentesis
print (tupla)
print (lista)
#segunda diferencia es que las tuplas son inmutables, es decir, que las listas
#pueden variar como ya vimos, pero las tuplas NO.
#las listas son los mismo que las variables. Mientras que las tuplas es lo
#mismo quye las constantes

#ventajas de las tuplas
"Lo que se define en la tupla no puede veriar, esto sera un elemento clave en seguridad"

#llamar a un elemento de una tupla
print(tupla[0])

#combinar elementos de una tupla
TuplaComb = (10,50,15, "El resultado de la operacion es:")
print(TuplaComb[3], TuplaComb[0] + TuplaComb[1] + TuplaComb[2])

#esto es solo una variable
Tupla1 = (10)
#para que sea una tupla se le debe agregar una coma
Tupla2 = (10,)
