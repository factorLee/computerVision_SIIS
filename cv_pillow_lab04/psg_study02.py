import PySimpleGUI as psg

menu = [
    "메뉴",
    ["파일", "편집", "보기", ["목록", "자세히", "전체"]]
]

layout = [
    [psg.ButtonMenu("메뉴 버튼", menu_def=menu)]
]

window = psg.Window("버튼메뉴 테스트", layout)

event, values = window.read()
window.close()
print(event, values)

