'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona. 
Esta información se le va a ir pidiendo al usuario el cual deberá completar los campos de “nombre”, “apodo” 
y “teléfono”. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario completo.'''

#definir diccionario vacio

persona = {}

#funcion añadir persona

def agregar_persona():

    dni=int(input("Agregar Dni"))
    nombre=str(input("Agregar nombre")) 
    apodo=str(input("Agregar apodo"))
    telefono=int(input("Agregar telefono"))
    
    #Creamos el diccionario con los datos de la persona
    
    datos_personal= {
        "nombre" : nombre,
        "apodo" : apodo,
        "telefono" : telefono
        
    }
    #Agregamos los datos de la persona al diccionario
    persona[dni] = datos_personal
    
    #Mostramos el diccionario con los datos cargados
    print("Datos personales cargados correctamente")
    print(persona)
    
#llamamos a la función para agregar persona

#opcion 1 cargar personas consultando la cantidad de registro que se va a cargar
cantidad_registro = int(input("ingrese la cantidad de personas a registrar"))
for numero in range(cantidad_registro):
    agregar_persona()
    