
from pickle import TRUE
import sys
from typing import Container
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton, QLabel, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #fixe le titre et la taille de la fenêtre principale 
        self.setWindowTitle("Da BinaryTron")
        self.setFixedSize(400,200)

        self.label = QLabel()
        self.input = QLineEdit("enter the int here")
        #ajout d'une seconde ligne pour mettre le resultat en binary 
        self.input2 = QLineEdit("expecting magic here !")
        self.button= QPushButton("Let's do some magic!")
        layout = QVBoxLayout()


        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.BinaryTransfo)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    #vérifier que la variable binary peut être transformée en int ! pas en float , ni en str  sinon message d'erreur
    def BinaryTransfo(self):
        if self.input.text().isdigit() == True:
            binary = self.input.text()
            self.input2.setText(bin(int(binary)))
        elif self.input.text().isdecimal == True: 
            self.input2.setText("no float just int !")
        else:
            self.input2.setText("Try with a int !")
        
        

        

BinaryTron = QApplication(sys.argv)

MainTron = MainWindow()
MainTron.show()

BinaryTron.exec()