
def get_todo(file_path):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(file_path, todos_arg):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
    

todos = []
file = open('todos.txt', "w")
file.close()

while True:
    user_action = input('Typer add, show, edit, complete or exit: ')
    user_action = user_action.strip(" ")
    
    
    if user_action.startswith('add'):
        
        # if len(user_action) > 4:
        todo =  user_action[4:]
        todos = get_todo('todos.txt')
        todos.append(todo + "\n")
        write_todos("todos.txt", todos)

        # elif len(user_action) <= 4:
        #     todo = input("Enter a ToDo: ") + "\n"
        
        #     todos = get_todo('todos.txt')
        
        #     todos.append(todo)
        
        #     write_todos("todos.txt", todo)
            
    elif user_action.startswith('show'):
        
        todos = get_todo('todos.txt')
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(f"You are editing ToDo number {number}")
            number = number - 1

            todos = get_todo()
            
            new_todo = input("Enter new ToDo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
                
        except ValueError:
            print("Your command is not valid")
            continue
    
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todo = get_todo('todos.txt')
            
            todo_to_remove = todos[number - 1].strip()
                
            todos.pop(number - 1)
            
            write_todos("todos.txt", todos)
            
            print(f'ToDo [{todo_to_remove}] was removed from list')   
            
        except IndexError:
            print("There is no item with that number")
            continue
    
    elif user_action.startswith('exit'):
        break
    
    else:
        pass
    
    
print('Bye')