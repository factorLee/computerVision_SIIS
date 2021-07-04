import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


column1 = [
    [psg.Checkbox("체크박스1", key="-CHECK1-")],
    [psg.Checkbox("체크박스2", key="-CHECK2-")],
    [psg.Checkbox("체크박스3", key="-CHECK3-")]

]

column2 = [
    [psg.Checkbox("체크박스A", key="-CHECKA-")],
    [psg.Checkbox("체크박스B", key="-CHECKB-")],
    [psg.Checkbox("체크박스C", key="-CHECKC-")]
]

layout = [
    [psg.Column(column1), psg.VerticalSeparator(), psg.Col(column2)],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

