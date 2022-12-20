import json
import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

file = open('data.json', 'r')
data = json.load(file)
randomlist=[]
for k in data:
    randomlist.append(k+' '+data[k])
interface = [
    [sg.Listbox(values=randomlist, size=(20, 10))],
    [sg.InputText(key='product', size=(20, 1))],
    [sg.InputText(key='num', size=(20, 1))],
    [sg.Button('Add'), sg.Button('Close')]
]

window = sg.Window('Warehouse Contents', interface, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event == 'Add':
        output = open('data.json', 'w')
        data[values['product']] = values['num']
        output.write(json.dumps(data))
        output.close()
    if event == 'Close' or event == WINDOW_CLOSED:
        break
