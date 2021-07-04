import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox



layout = [
    [psg.Image("./skyline.png")],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

