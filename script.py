import json
import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

file = open('data.json', 'r')
data = json.load(file)

interface = [
    [sg.Listbox(values=data[0], size=(20, 10))],
    [sg.InputText(key='product', size=(20, 1))],
    [sg.InputText(key='num', size=(20, 1))],
    [sg.Button('Add'), sg.Button('Edit'), sg.Button('Close')]
]

window = sg.Window('Warehouse Contents', interface, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'Add':
        output = open('data.json', 'w')
        data[0][values['product']] = values['num']
        output.write(json.dumps(data))
        output.close()
    if event == 'Edit':
        output = open('data.json', 'w')
        data[0][values[[0]]] = values['num']
        output.write(json.dumps(data))
        output.close()
    if event == 'Close' or event == WINDOW_CLOSED:
        break
