import json
import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

file = open('data.json')
data = json.load(file)

interface = [[sg.Listbox(values=data, size=(20, 10))],
    [sg.InputText(key='product', size=(20, 1))],
    [sg.InputText(key='num', size=(20, 1))],
    [sg.Button('Add'), sg.Button('Edit'), sg.Button('Close')]]

window = sg.Window('Warehouse Contents', interface, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'Add':
        data[0][values['product']]=values['num']
        json.dump(data, file)
    if event == 'Edit':
        data[0][values[[0]]] = values['num']
        json.dump(data, file)
    if event == 'Close' or event == WINDOW_CLOSED:
        break