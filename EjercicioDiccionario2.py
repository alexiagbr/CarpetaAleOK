# El programa pedira el numero de alumnos que vamos a introducir, pedira su nombre e ira
# pidiendo sus notas hasta que introduzcamos un "numero negativo"
# Al final el programa nos mostrara la lista de alumnos y la nota media obtenida por cada uno
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dara un error

alumno = {} #diccionario vacio
cantidad = int(input("Ingrese la cantidad de alumnos a cargar sus notas"))
for num in range (cantidad):
    alum= input ("Ingrese el nombre del alumno: ")
    while alum in alumno:
        print ("El alumno ya existe")
        alum = input ("Ingrese el nombre del alumno")
    notas =[]
    nota= float (input ("Ingrese la nota negativa para salir"))
    while nota > 0:
        notas.append (nota)
        nota= float (input ("Ingrese la nota negativa para salir"))
    alumno [alum]= nota.copy() #completando el cuestionario


for alum, notas in alumno.items():
    print(f" Ha sacado nota promedio ",(alum, sum(notas)/len(notas)))  #recorre el diccionario y va mostrando las notas promedios de los alumnos

