"""Escribir un codigo en el cual se comience con una lista vacia
y se le pregunte al usuario el tratamiento que se le quiere dar. Si el usuario ingresa "pila" 
se debera eliminar y mostrar uno a uno en el orden convencional de la pila.
Hacer los mismo pero en el orden de la cola para el caso que ingrese "Cola".
Pensar para que la estructura utilizariamos una pila o cola en algun ejemplo cotidiano"""

lista = []

tratamiento = input("Ingrese 'pila' o 'cola': ")

if tratamiento == 'pila':
    while lista:
        elemento = lista.pop()
        print(elemento)

elif tratamiento == 'cola':
    while lista:
        elemento = lista.pop(0)
        print(elemento)

else:
    print("Ingrese 'pila' o 'cola'.")
    
# tareas diarias
cola_tareas_diarias = []

# menu tareas diarias a la cola
cola_tareas_diarias.append("Levantarse a las 7:00 am")
cola_tareas_diarias.append("Desayunar")
cola_tareas_diarias.append("Ir al trabajo")
cola_tareas_diarias.append("Almuerzar")
cola_tareas_diarias.append("Regresar a casa")
cola_tareas_diarias.append("Cenar")
cola_tareas_diarias.append("Dormir")

print("Tareas diarias:")
for tarea in cola_tareas_diarias:
    print(tarea) 
    
