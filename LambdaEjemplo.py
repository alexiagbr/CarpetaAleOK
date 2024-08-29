# Ejemplo 1
(lambda nombre: print(f"hola {nombre}"))("Pedro")
 
 #Ejemplo 2
#colores = ["rojo", "azul","verde", "amarillo"]
(lambda color :print(f"el color se encuentra en la posición  {colores.index(color)} de la lista")) ("verde")
 
# Ejemplo 3

multiplicacion= lambda numero1, numero2 : numero1 * numero2

resultado = multiplicacion (10,5)
resultado1= multiplicacion(8,2)

print(resultado)
print(resultado1)

#Ejemplo 4
mayuscula = lambda cadena : cadena.upper()
print (mayuscula ("rodrigo"))

# Ejemplo 4
positivo = lambda x : "El numero es positivo" if x>0 else "El numero es negativo"
print (positivo(4))

# Ejemplo 5
mayor_edad = lambda edad : "Eres mayor de edad " if edad>=18 else "Eres menor de edad"
edad = int(input("ingrese tu edad"))
resultado_edad = mayor_edad (edad)
print(resultado_edad)

#Ejemplo 6
lista = [20, 15, -4,5,-1, 12,-3]
lista_positivos =list(filter (lambda x: x>=0, lista ))
print (lista_positivos)

#Ejemplo 7
lista=[1,2,3,4,5,6,7,8,9,10]
lista_duplicar = list(map(lambda x : x*3, lista))
print(lista_duplicar)