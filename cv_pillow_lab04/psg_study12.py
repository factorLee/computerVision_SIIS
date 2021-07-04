import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.Multiline(size=(100,20))],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("메뉴 테스트", layout, size=(200,200))

event, values = window.read()
window.close()
print(event, values)

