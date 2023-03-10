import json
import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

file = open('data.json', 'r')
data = json.load(file)
randomlist=[]
for k in data:
    randomlist.append(k+' '+data[k])
interface = [
    [sg.Listbox(values=randomlist, key='box', size=(20, 10))],
    [sg.Text("Vare:"), sg.InputText(key='product', size=(20, 1))],
    [sg.Text("Antal:"), sg.InputText(key='num', size=(20, 1))],
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
        randomlist = []
        for k in data:
            randomlist.append(k + ' ' + data[k])
        window['box'].update(randomlist)
    if event == 'Close' or event == WINDOW_CLOSED:
        break
