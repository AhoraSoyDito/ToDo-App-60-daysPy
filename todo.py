def obeter_tareas(ruta = "todos.txt"):
    with open (ruta, "r") as f:
        tareas = f.readlines()
    return tareas

def escribir_tareas(tareas_arg, ruta = "todos.txt"):
    with open (ruta, "w") as f:
        f.writelines(tareas_arg)
