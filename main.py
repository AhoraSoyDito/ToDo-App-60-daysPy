todos = []
while True:
    user_action = input('Typer add, show, edit, complete or exit: ')

    user_action = user_action.strip(" ")
    
    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ") + "\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show':
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            
            #new_todos = [item.strip('\n') for item in todos]
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item}"
                print(row)
                
        case 'edit':
            number = int(input("Number of the ToDo to edit: "))
            number = number - 1
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            new_todo = input("Enter new ToDo: ")
            todos[number] = new_todo + "\n"
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            todo_to_remove = todos[number - 1].strip()
                
            todos.pop(number - 1)
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)
                
                
            print(f'ToDo {todo_to_remove} was removed from list')    
        case 'exit':
            break
        
    
print('Bye')