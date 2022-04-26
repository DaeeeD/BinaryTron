
from cgi import test
import sys
from tkinter import Button
from binaryTransfo import *

from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Binary Transotron")
        self.edit = QLineEdit("enter the binary: ")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)


if __name__== '__main__':
    app = QApplication(sys.argv)
    Button = QPushButton("Let the magic begin!")
    Button.clicked.connect(binary_transfrom)
    form = Form()
    form.show()
    sys.exit(app.exec())

