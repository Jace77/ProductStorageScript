import json
import PySimpleGUI as sg

file = open('data.json')
data = json.load(file)

interface = [[sg.Listbox(values=data, size=(20, 50))],
    [sg.InputText(key='product', size=(20, 1))],
    [sg.InputText(key='num', size=(20, 1))],
    [sg.Button('Save'), sg.Button('Close')]]

window = sg.Window('Warehouse Contents', interface, margins=(100, 100))
window.read()

while True:
    event, values = window.read()
    if event =='Close':
        break
    if event == 'Save':
        data[0][values['product']]=values['num']