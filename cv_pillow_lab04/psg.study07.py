import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


data = list("abcdefg")
# ["a","b","c","d","e","f","g"]

frame = [
    [psg.Combo(values=data, size=(10,4), default_value=data[2])],
    [psg.HorizontalSeparator()],
    [psg.CB("체크박스1"), psg.CB("체크박스2")]
]

layout = [
    [psg.Frame("프레임 테스트", frame)],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

