import PySimpleGUI as psg


# 레이아웃을 줄 때 리스트 형태로 준다.
layout = [
    [psg.Button('버튼', size=(10,2))], 
    [psg.Btn('버튼2', size=(10,2), button_color=("blue", "green"))],
    [psg.B("버튼3")],
    [psg.Ok(), psg.Cancel()],
    [psg.Yes(), psg.No()]
]
window = psg.Window("버튼 처리 학습", layout)

event, values = window.read()
window.close()
print(event, values)