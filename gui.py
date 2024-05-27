import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a ToDo", key="todo")
add_button = sg.Button("Add")
window = sg.Window("My ToDO App", 
                    layout=[[label], [input_box, add_button ]], 
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
        case sg.WIN_CLOSED:
            break
    
window.close()

