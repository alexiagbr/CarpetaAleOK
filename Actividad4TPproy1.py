 #Definición del diccionario principal para la base de datos de clientes
clientes = {}

# Función para añadir  un cliente
def agregar_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    
    # Creamos un diccionario con los datos del cliente
    datos_cliente = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo
    }
    
    # Agregamos el cliente al diccionario principal
    clientes[dni] = datos_cliente
    
    # Mostramos el diccionario de clientes actualizado
    print("Cliente añadido correctamente.")
    print("Base de datos actualizada:")
    print(clientes)

#Función para eliminar un cliente
#b)Pedir un DNI y eliminar al cliente. En caso de que no exista, debe avisarlo por mensaje. 
def eliminar_cliente():
    dni = input("Ingrese el DNI del cliente que desea eliminar: ")
    
    # Verificamos si el cliente está en la base de datos
    if dni in clientes:
        del clientes[dni]
        print(f"Cliente con DNI {dni} eliminado correctamente.")
        print("Base de datos actualizada:")
        print(clientes)
    else:
        print(f"No se encontró ningún cliente con DNI {dni} en la base de datos.")

# Función para mostrar los datos de un cliente
#c) Pedir un DNI y mostrar los datos en un mensaje (por ejemplo “nombre:x, apellido:y….”). 
# Mostrar mensaje de error si no lo encuentra. 
def mostrar_cliente():
    dni = input("Ingrese el DNI del cliente que desea mostrar: ")
    
    # Verificamos si el cliente está en la base de datos
    if dni in clientes:
        datos = clientes[dni]
        print(f"Datos del cliente con DNI {dni}:")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Correo electrónico: {datos['correo']}")
    else:
        print(f"No se encontró ningún cliente con DNI {dni} en la base de datos.")

# Función para terminar el programa
#d) Vaciar el diccionario, mostrarlo y mostrar mensaje de despedida. 

def terminar_programa():
    # Vaciamos el diccionario de clientes
    clientes.clear()
    print("Base de datos de clientes vaciada.")
    print("Base de datos actualizada:")
    print(clientes)
    print("¡Hasta luego!")

# Menú principal del programa
while True:
    print("-----------------------------")
    print("\n--- Menú de opciones ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Terminar")
    print("-----------------------------")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        agregar_cliente()
    elif opcion == '2':
        eliminar_cliente()
    elif opcion == '3':
        mostrar_cliente()
    elif opcion == '4':
        terminar_programa()
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-4).")