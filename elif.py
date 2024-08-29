"""elif puede verifica varias condiciones al incluir una o mas verificaciones elif despues de la 
declaracion del if inicial. Solo se ejecuta con una condicion"""

edad = int(input("Ingrese la edad: "))
if edad>9:
    print("la edad es la opcion 1: ", edad)
elif edad >6:
    print ("la edad es la opcion 2: ", edad)
elif edad >3:
    print ("la edad es la opcion 3: ", edad)
else:
    print ("la edad es la opcion 4 :", edad)