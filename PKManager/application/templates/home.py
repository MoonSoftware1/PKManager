import json
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QTextEdit, QShortcut, QPushButton
from PyQt5.Qt import Qt, pyqtSignal, pyqtSlot, QObject, QKeySequence
from application.packages.PYBox import PYBox


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

        self.text_box = QTextEdit(self)
        self.text_box.setStyleSheet("color: #ffffff; font-size: 15px; border: 0px; background-color: transparent")
        self.text_box.setAlignment(Qt.AlignTop)
        self.text_box.setGeometry(0, 0, 750, 375)

        options = QPushButton("Options", self)
        options.setStyleSheet("font-family: Roboto; font-size: 12px; font-style: normal; font-weight: 400;"
                              "line-height: normal; color: rgb(255, 255, 255); background-color: transparent")
        options.setGeometry(0, 375, 75, 25)

        view = QPushButton("View", self)
        view.setStyleSheet("font-family: Roboto; font-size: 12px; font-style: normal; font-weight: 400;"
                              "line-height: normal; color: rgb(255, 255, 255); background-color: transparent")
        view.setGeometry(75, 375, 75, 25)

        help = QPushButton("Help", self)
        help.setStyleSheet("font-family: Roboto; font-size: 12px; font-style: normal; font-weight: 400;"
                              "line-height: normal; color: rgb(255, 255, 255); background-color: transparent")
        help.setGeometry(150, 375, 75, 25)

        quit = QPushButton("Quit", self)
        quit.setStyleSheet("font-family: Roboto; font-size: 12px; font-style: normal; font-weight: 400;"
                              "line-height: normal; color: rgb(255, 255, 255); background-color: transparent")
        quit.setGeometry(225, 375, 75, 25)
