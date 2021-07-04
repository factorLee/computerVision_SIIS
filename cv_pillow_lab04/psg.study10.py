import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox

data = list("abcdefg")

layout = [
    [psg.Listbox(values=data, size=(20,4))],
    
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

