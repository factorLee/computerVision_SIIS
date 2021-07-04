import sys

from PIL import Image, ImageQt
from PyQt5.QtWidgets import  QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QApplication


class ImageViewer(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt Image Viewer")

        # open up image in Pillew
        #image = Image.open("Pink_flower.jpg")
        image = Image.open("hummingbird.jpg")
        pixmap = ImageQt.toqpixmap(image)

        self.image_label = QLabel('')
        self.image_label.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    app.exec_()