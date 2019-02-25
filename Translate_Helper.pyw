#!/usr/bin/python3
import sys
import subprocess
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication, QRect


class Ui_Form(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.path = os.getcwd()
        self.setWindowTitle("Translate helper")
        self.setWindowIcon(QtGui.QIcon(self.path + '\\logo.png'))
        self.resize(640, 480)
        self.cut = QPushButton("Вырезать строки", self)
        self.cut.setGeometry(QRect(20, 50, 111, 41))
        self.cut.setObjectName("cut")
        self.cut.clicked.connect(lambda:self.launch(self.path +'\\loc_cutter.pyw'))
        #------------------------------------------------
        self.put = QPushButton("Вставить строки", self)
        self.put.setGeometry(QRect(20, 290, 111, 41))
        self.put.clicked.connect(lambda:self.launch(self.path +'\\loc_putter.pyw'))
        #------------------------------------------------
        self.tr = QPushButton("Быстрый перевод", self)
        self.tr.setGeometry(QRect(20, 170, 111, 41))
        self.tr.clicked.connect(lambda:self.launch(self.path +'\\loc_translate.pyw'))
        #------------------------------------------------
        self.label_1 = QLabel("<html><head/><body><p>Вырезает строки с переводом из файла локализации и переносит </p><p>их в файл rus_названиемода_l_english.yml</p></body></html>", self)
        self.label_1.setGeometry(QRect(160, 50, 411, 41))
        #------------------------------------------------
        self.label_2 = QLabel("<html><head/><body><p>Берёт файл из первого пункта и вставляет переведённые строки обратно.</p><p>(Выбирать изначальный файл)</p><p>(Создаёт новый файл на основе изначального с приставкой final_)</p></body></html>", self)
        self.label_2.setGeometry(QRect(160, 280, 451, 71))
        #------------------------------------------------
        self.label_3 = QLabel("<html><head/><body><p>На основе файла с вырезанными строками создаёт файл </p><p>с машинным переводом от GT для ориентировки при переводе.</p><p>(Выбирать файл с приставкой rus_)</p></body></html>", self)
        self.label_3.setGeometry(QRect(160, 160, 441, 71))
        #------------------------------------------------
        self.exit = QPushButton("Выход", self)
        self.exit.setGeometry(QRect(20, 410, 111, 41))
        self.exit.clicked.connect(sys.exit)
        self.show()

    def launch(self, script):
        subprocess.call([sys.executable, script])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form()
    sys.exit(app.exec_())