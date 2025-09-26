import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from io import BytesIO
import requests
from PIL import Image


class MainWindow(QMainWindow):
    g_map: QLabel

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('main_window.ui', self)
        self.spn = 0.005
        self.x = 37.588392
        self.y = 55.734036
        self.file = file
        self.get_map()

    def get_map(self):
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        map_params = {
            "ll": f"{self.x},{self.y}",
            "spn": f"{self.spn},{self.spn}",
            "l": "map",
        }

        response = requests.get(map_api_server, params=map_params)
        Image.open(BytesIO(response.content)).save('map.png')
        self.file = "map.png"
        pixmap = QPixmap(self.file)
        self.label.setPixmap(pixmap)
        self.label.setFixedSize(795, 595)

    def keyPressEvent(self, event):
        try:
            delta = 0
            if event.key() == Qt.Key_PageUp:
                delta = 0.01
            elif event.key() == Qt.Key_PageDown:
                delta = - 0.01
            self.spn += delta
            self.get_map()
        except:
            self.spn -= delta

        if event.key() == Qt.Key_Left:
            self.x -= 0.01
        elif event.key() == Qt.Key_Right:
            self.x += 0.01
        elif event.key() == Qt.Key_Down:
            self.y -= 0.01
        elif event.key() == Qt.Key_Up:
            self.y += 0.01
        self.get_map()


file = 'map.png'
app = QApplication(sys.argv)
main_window = MainWindow(file)
main_window.show()
sys.exit(app.exec())
