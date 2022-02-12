from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

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
window.show()

app.exec();

