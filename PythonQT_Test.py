from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from QtDesigner_File.MainPage import Ui_Form

import os
#import gphoto2 as gp
import subprocess
import sysconfig
#import cv2


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('QtDesigner_File/MainPage.ui', self)

        self.setWindowTitle ("Python11")
        self.window.__init__()
        


    def exit(self):
        print('Exit')
        quit()

    def test(self):
        print('Test')
       # camera = gp.Camera()
       # config_tree = camera.get_config()
       # print(config_tree)


app = QApplication([])

window = Ui()
ui = Ui_Form()
ui.setupUi(window)

#ui.btExit.clicked.connect(Ui.prova)

window.show()

app.exec();

