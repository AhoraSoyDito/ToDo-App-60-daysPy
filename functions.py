

def get_todos(file_path = "todos.txt"):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, file_path = "todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
    