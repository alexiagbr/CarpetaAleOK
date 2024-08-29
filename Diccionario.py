' escribir un programa que pregunte al usuario '
' su nombre, edad, direccion y telefono y lo guardo en un diccionario. '
' Despues debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,'
' vive en direccion y su numero de telefono es <telefono>.'

#sintaxis //
#nombre_diccionario = {"clave": valor , "clave1": valor1; "clave2": valor2"}

nombre = input('¿Como te llamas?')
edad = input('¿Cuantos años tienes?')
direccion = input('¿Cual es tu direccion?')
telefono = input('¿Cual es tu telefono?')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'],'tiene', persona['edad'],'años,vive en',persona['direccion'])
