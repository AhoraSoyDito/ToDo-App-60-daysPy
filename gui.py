import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a ToDo",)

window = sg.Window("My ToDO App", layout=[[label], [input_box, ]])
window.read()
window.close()