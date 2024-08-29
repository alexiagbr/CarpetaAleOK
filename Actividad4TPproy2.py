"""En este proyecto, vas a desarrollar un sistema para gestionar tareas. El sistema permitirá agregar 
nuevas tareas, actualizar su descripción y prioridad, marcarlas como completadas, eliminarlas, y listar 
tanto las tareas pendientes como las completadas. Deberás escribir pruebas unitarias utilizando pytest para 
asegurar que todas las funciones del sistema funcionan correctamente."""

tareas = {}
def agregar_tarea(id_tarea, descripcion, prioridad):
    if id_tarea in tareas:
        raise ValueError ("La tarea con este ID ya existe")
    tareas[id_tarea]={
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    
def actualizar_tareas(id_tarea, nueva_descripcion, nueva_prioridad):
    if id_tarea not in tareas:
        raise KeyError ("La tarea no existe")
    tareas[id_tarea]["descripcion"]= nueva_descripcion
    tareas[id_tarea]["prioridad"]= nueva_prioridad
    
    
def marcar_completada(id_tarea):
    if id_tarea not in tareas:
        raise KeyError ("La tarea no existe")
    tareas[id_tarea]["completada"]= True
    
def eliminar_tarea(id_tarea):
    if id_tarea not in tareas:
        raise KeyError ("La tarea no existe")
    del tareas[id_tarea]
    
def lista_tarea():
    if id_tarea not in tareas:
        

    
    
    
agregar_tarea(1, "limpiar", "alta")
print(tareas)
    
        