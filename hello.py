''' import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QInputDialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Binarytron')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        #formLayout.addRow('Numbertransformtron:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_()) '''


import sys
from typing import Container
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton, QLabel, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Da BinaryTron")

        self.label = QLabel()

        self.input = QLineEdit()

        self.button= QPushButton("Let do some magic!")

        layout = QVBoxLayout()


        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.BinaryTransfo)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

#vérifier que la variable binary peut être transformée en int ! sinon message d'erreur 
    def BinaryTransfo(self):
        binary = self.input.text()
        self.input.setText(bin(int(binary)))
        
        

        

BinaryTron = QApplication(sys.argv)

MainTron = MainWindow()
MainTron.show()

BinaryTron.exec()