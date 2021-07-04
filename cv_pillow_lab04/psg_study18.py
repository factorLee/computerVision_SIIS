import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.Multiline(size=(50,50))],
    [psg.StatusBar("안녕하세요!")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Status 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

