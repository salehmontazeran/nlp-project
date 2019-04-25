from os import path

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout, QLabel, QMessageBox,
                             QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from languages.lang import lang
from nlptools.kernels import engtopic, fatopic

from .BaseWindow import BaseWindow


class TopicWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.lang = l
        self.title = self.title + ' - ' + lang[l]["topic"]
        # self.width = self.width / 2
        # self.height = self.height / 2
        self.inFile = ""
        self.output = ""
        self.basicInit()
        self.setup()
        self.show()

    def setup(self):
        myFont = QFont("Calibri")
        myFont.setPointSize(14)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        firstLayout = QHBoxLayout()

        self.firstLable = QLabel(lang[self.lang]["inputSelect"], self)
        self.firstLable.setFont(myFont)
        self.firstPush = QPushButton(lang[self.lang]["browse"], self)
        self.firstPush.setFont(myFont)
        firstLayout.addWidget(self.firstLable)
        firstLayout.addStretch()
        firstLayout.addWidget(self.firstPush)
        self.firstPush.clicked.connect(self.selectFile)

        thirdLayout = QVBoxLayout()
        thirdLayout.addStretch()
        thirdLayout.addLayout(firstLayout)

        self.thirdPush = QPushButton(lang[self.lang]["topicfa"], self)
        self.thirdPush.setFont(myFont)
        self.thirdPush.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.thirdPush.clicked.connect(self.topicfa)

        self.forthPush = QPushButton(lang[self.lang]["topicen"], self)
        self.forthPush.setFont(myFont)
        self.forthPush.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.forthPush.clicked.connect(self.topicen)

        thirdLayout.addStretch()
        thirdLayout.addStretch()
        thirdLayout.addStretch()
        thirdLayout.addWidget(self.thirdPush)
        thirdLayout.addWidget(self.forthPush)

        wid.setLayout(thirdLayout)

    @pyqtSlot()
    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, lang[self.lang]["inputSelect"], "", "All Files (*)"
        )
        if fileName:
            self.firstPush.setText(path.basename(fileName))
        self.inFile = fileName

    @pyqtSlot()
    def topicfa(self):
        fileExist = path.isfile(self.inFile)
        if fileExist:
            with open(self.inFile, 'r', encoding="utf8") as f:
                text = f.read()
                ans = fatopic.predict(text)
                QMessageBox.information(self, " ", str(ans))
        else:
            QMessageBox.warning(self, " ", lang[self.lang]["fail"])

    @pyqtSlot()
    def topicen(self):
        fileExist = path.isfile(self.inFile)
        if fileExist:
            with open(self.inFile, 'r') as f:
                text = f.read()
                ans = engtopic.predict(text)
                QMessageBox.information(self, " ", str(ans))
        else:
            QMessageBox.warning(self, " ", lang[self.lang]["fail"])
