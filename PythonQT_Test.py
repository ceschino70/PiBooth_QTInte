from PyQt5.QtWidgets import * # QApplication, QWidget, Q
from PyQt5 import uic
from QtDesigner_File.MainPage import Ui_Form
#prova

import os
import gphoto2 as gp
import subprocess
import sysconfig


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('QtDesigner_File/MainPage.ui', self)

        self.setWindowTitle ("Python11")
        self.UiComponents()

    def exit(self):
        print('Exit')
        quit()

    def test(self):
        print('Test')
        camera = gp.Camera()
        config_tree = camera.get_config()
        print(config_tree)

    def UiComponents(self):
        button = QPushButton("CLICK", self)
        button.setGeometry(200,150,100,30)
        button.clicked.connect(self.clickme)
        button.setText("Over-write")

    def clickme(self):
        # printing pressed
        print("pressed")

app = QApplication([])

window = Ui()
ui = Ui_Form()
ui.setupUi(window)

#ui.btExit.clicked.connect(Ui.prova)

window.show()

app.exec();

