#escribir un programa que le pregunte al usuario 
# nombre , edad, direccion y lo guarde en un diccionarios
#mostrar por pantalla el diccionario... 

nombre = str(input ("ingrese el nombre"))
edad= int(input(" ingrese la edad "))
direccion= str(input(" ingrese la direccion ")) 

usuario = {"nom": nombre, "edad": edad, "direccion": direccion}
print(usuario)

print(usuario["nom"], "tiene ", usuario ["edad"], "años  y vive en la dirección", usuario["direccion"])


   