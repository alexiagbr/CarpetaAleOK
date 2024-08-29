"""La AFA tiene conocimiento que son tres estadios los más grandes de Argentina. Se necesita un programa que
ingrese el nombre del estadio y la capacidad de cada uno, y determine cuál es el mayor de todos."""

#definimos la variable de los nombres de los estadios

Estadio1=(str(input ("¿nombre del estadio 1?")))
capacidad1=(float(input ("ingrese capacidad de estadio")))

Estadio2=(str(input ("nombre del estadio 2")))
capacidad2=(float(input("ingrese capacidad de estadio")))

Estadio3=(str(input ("¿nombre del estadio 3?")))
capacidad3=(float(input ("ingrese capacidad de estadio")))

if capacidad1 > capacidad3:
    mayor_capacidad = capacidad1
    print("El estadio con mayor capacidad es", Estadio1, "con una capacidad de", capacidad1)
else:
    mayor_capacidad = capacidad3
    print("El estadio con mayor capacidad es", Estadio3, "con una capacidad de", capacidad3)
    
else:
    if capacidad2 > capacidad3:
    mayor_capacidad = capacidad2
    print("el estadio con mayor capacidad es", Estadio2, "con una capacidad de", capacidad2)
else
mayor_capacidad = capacidad3
    print("el estadio con mayor capacidad es", Estadio3, "con una capacidad de", capacidad3)
    
    
    