import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.Output(size=(100,20))],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Output 테스트", layout, )

event, values = window.read()
if event == "Ok":
    for i in range(100):
        print(i)

window.close()
print(event, values)

