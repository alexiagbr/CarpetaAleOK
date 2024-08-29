#Condicional  - it
#Operadores de comparacion
#> mayor
#< menor
#>= mayor igual
#<= menor igual

# #ejemplo N°1
precio=0


precio= int(input("ingrese precio"))
if precio>500:
      print ("tiene descuento")
else:
   print ("no tiene descuento")

#igual ==
if precio == 500:
    print("tiene descuento")
else:
        print ("no tiene descuento")

# if caracteres o texto
#upper () devuelve una cadena en mayuscula
#lower () devuelve una cadena en minuscula
#capitaize () devuelve una la primera letra en mayuscula
lenguaje=(str(input ("¿cual lenguaje de programacion estas estudiando?"))).capitalize()
if lenguaje == "Python":
    print("Excelente")
else:
     print("Mala eleccion")    

#evaluar con una boolean

usuario=True
if usuario:
      print ("verdadero")
else:
      print ("falso")


#anidados
num3 = int (input("Ingrese un numero: "))
if num3 % 2 == 0:  #comprueba si el numero es par
      if num3 > 10:
            print ("El numero es mayor de 10 y es par", num3)
      else:
            print ("El numero no es mayor que 10, pero es par ", num3)
else:
            print("El numero no es par ", num3)
      

                  
