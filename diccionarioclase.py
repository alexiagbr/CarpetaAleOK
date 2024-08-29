# Diccionarios distintos tipos de datos y formados por llave (key) y valor
# estructuras de datos mutables
# los diccionarios llevan llaves {} y la coma  clave:valor ,   

diccionario = {
    "nombre": "Juan",
    "apellido":"Perez",
    "edad": 25,
    "estatura": 1.75,
    "hobbies": ["leer", "dormir", "jugar"],
    "direccion": {
        "calle": "Av. Siempre Viva",
        "numero": 123
    }
}
print(diccionario)

print(diccionario ["nombre"])
