# realice un programa que nos permita guardar los nombre de los alumnos de una clase
#y las notas  que han obtenido. Cada Alumnos puede tener distintas cantidad de notas .
#Guarda la informacion diccionario cuya clave seran los nombre de los alumnos
# y los valores seran listas con las notas de cada alumnos

#el programa pedira la cantidad alumnos a registrar y el nombnre los mismos
# para terminar la carga de las notas debe solicitar un nota negativa. 
#al finalizar mostrar la lista de alumnos y nota promedio
# Si introduce un alumnos que ya existe  el programa nos dara un mensaje. 

alumnos={} # creamos diccionario vacio
cantidad=int(input("ingrese la cantidad de alumnos a registrar"))

for num in range(cantidad):
    nombre=str(input("Ingrese el nombre del alumno:  "))
    while nombre in alumnos: # si el nombre se encuentra en el diccionario
        print("El alumno ya existe")
        nombre=str(input("Ingrese el nombre del alumno:  ")) # vuelve a solicitar el ingreso del nombre 
    notas=[] # creo lista vacia para las notas
    nota=float(input(" Ingrese la nota del alumno (negativo para terminar: )"))
    while nota > 0: 
        notas.append(nota)
        nota=float(input(" Ingrese la nota del alumno (negativo para terminar: )"))
    alumnos[nombre]=notas.copy() # llenamos el diccionario con las notas guardas en la lista

for nombre, notas in alumnos.items(): # muestra el diccionario con las notas 
    print(" Se ha sacado la nota promedia " ,(nombre, sum(notas)/len(notas)))


