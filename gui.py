import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")

input_box = sg.InputText(tooltip="Enter a ToDo", key="todo")

add_button = sg.Button("Add")

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

list_box = sg.Listbox(values = functions.get_todos(),
                        key= "todos",
                        enable_events = "True",
                        size=[45,10])





window = sg.Window("My ToDO App", 
                    layout=
                    [
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]
                    ], 
                    font=('Times New Roman', 10) )



while True:

    event, values = window.read()
    print(values)
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values = todos)
        
        case "Edit":
            todo_to_edit = values['todos'][0]   
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            
            window["todos"].update(values = todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values = todos)
            window["todo"].update(value = "")]
            
        case "Exit":
            break
            
            
        case "todos":
            window["todo"].update(value = values['todos'][0])
        
        
        
        case sg.WIN_CLOSED:
            break
    
window.close()

