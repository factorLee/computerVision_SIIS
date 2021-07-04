import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.Spin(initial_value=3, values=list(range(1,10)), size=(5,5))],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

