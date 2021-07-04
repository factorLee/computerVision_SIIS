import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox



layout = [
    [psg.Text("입력1")],
    [psg.Input(key="-IN1-")],
    [psg.Text("입력2"), psg.Input(key="-IN2-")], 
    [psg.Text("입력3"), psg.Input(key="-IN3-")],
    
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

