import json
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame
from PyQt5.Qt import Qt


def collect_data():
    with open("data/configurations.json", "r") as file:
        configurations = json.load(file)
    return configurations


class HOMETemplate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = collect_data()

        self.setWindowTitle("PKManager - Home")
        self.setStyleSheet("background-color: #0F0F0F")
        self.setFixedSize(750, 400)
        self.initUI()

    def initUI(self):
        title = QLabel("MOON SOFTWARE", self)
        title.setStyleSheet("font-family: Roboto; font-size: 48px; font-style: normal; font-weight: 900;"
                            "line-height: normal; color: rgba(255, 255, 255, 0.15);")
        title.setGeometry(0, 0, 750, 400)
        title.setAlignment(Qt.AlignCenter)

        bottom_bar = QFrame(self)
        bottom_bar.setStyleSheet("border-top: 1px solid #848484; flex-shrink: 0;")
        bottom_bar.setGeometry(0, 375, 750, 25)

        version = QLabel("Version : {}".format(self.config['application']['version']), self)
        version.setStyleSheet("font-family: Roboto; font-size: 12px; font-style: normal; font-weight: 300;"
                              "line-height: normal; color: rgb(255, 255, 255); background-color: transparent")
        version.setGeometry(568, 375, 177, 25)
        version.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
