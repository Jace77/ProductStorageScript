import json
import PySimpleGUI as sg
interface = [[sg.Text('', size=(20, 1)), sg.InputText()],
             [sg.Text('', size=(50, 1), key='output', text_color="red")],
             [sg.Button('Save'), sg.Button('Close')]]

window = sg.Window('Spejdersport', interface, margins=(100, 100))
window.read()

while True:
    event, values =window.read()
    if event =='Close' or event == sg.WINDOW_CLOSED():
        break
if event == 'Save':
