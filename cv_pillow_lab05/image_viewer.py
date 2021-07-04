import io   # Python Standard Library
import os   # Python Standard Library
import PySimpleGUI as sg # 그래픽 인터페이스
from PIL import Image

# (), {}, [] 데이터 집합들을 만든다.
file_types = [("JPG(*.jpg)", "*.jpg"),
("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25,1), key="-FILE-"),
            sg.FileBrowse(file_types = file_types),
            sg.Button("Load Image"),
        ]
    ]
    window = sg.Window("이미지 뷰어", layout)

    # 이벤트 루트: while 무한루프 
    # 계속해서 사용자의 입력을 기다리고 있다.
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"] # layout에 input으로 반은 key값을 받음
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400,400)) # 400, 400 크기로 보여줌
                bio = io.BytesIO() # 메모리에 읽어오는 방법
                image.save(bio, format="PNG") # 저장
                window["-IMAGE-"].update(data=bio.getvalue()) # 윈도우에서 보여준다.

# 엔트리 포인트
if __name__ == "__main__": # dunder = double underscore _(single underscore), __(double underscore) / 앞에만? 뒤에만? 양쪽?
    main()
