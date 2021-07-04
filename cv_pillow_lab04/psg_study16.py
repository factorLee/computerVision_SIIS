import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.Slider(range=(1,101), default_value=50, orientation="v")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

