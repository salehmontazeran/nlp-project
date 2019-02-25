from os import path
from .BaseWindow import BaseWindow
from languages.lang import lang
from PyQt5.QtWidgets import QFileDialog, QLabel, QHBoxLayout, QPushButton, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSlot
from ..kernels.tokenization import Tokenization


class TokenizationWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.lang = l
        self.title = self.title + ' - ' + lang[l]["token"]
        # self.width = self.width / 2
        # self.height = self.height / 2
        self.inFile = ""
        self.output = ""
        self.basicInit()
        self.setup()
        self.show()

    def setup(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        firstLayout = QHBoxLayout()
        secondLayout = QHBoxLayout()

        self.firstLable = QLabel(lang[self.lang]["inputSelect"], self)
        self.firstPush = QPushButton(lang[self.lang]["browse"], self)
        firstLayout.addWidget(self.firstLable)
        firstLayout.addStretch()
        firstLayout.addWidget(self.firstPush)
        self.firstPush.clicked.connect(self.selectFile)

        self.secondLabel = QLabel(lang[self.lang]["outputSelect"], self)
        self.secondPush = QPushButton(lang[self.lang]["browse"], self)
        secondLayout.addWidget(self.secondLabel)
        secondLayout.addStretch()
        secondLayout.addWidget(self.secondPush)
        self.secondPush.clicked.connect(self.selectDir)

        thirdLayout = QVBoxLayout()
        thirdLayout.addLayout(firstLayout)
        thirdLayout.addLayout(secondLayout)

        self.thirdPush = QPushButton(lang[self.lang]["token"], self)
        self.thirdPush.clicked.connect(self.compute)

        thirdLayout.addStretch()
        thirdLayout.addWidget(self.thirdPush)

        wid.setLayout(thirdLayout)

    @pyqtSlot()
    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, lang[self.lang]["inputSelect"], "", "All Files (*)")
        if fileName:
            self.firstPush.setText(path.basename(fileName))
        self.inFile = fileName

    @pyqtSlot()
    def selectDir(self):
        dirName = QFileDialog.getExistingDirectory(self, lang[self.lang]["outputSelect"])
        if dirName:
            self.secondPush.setText(path.basename(path.normpath(dirName)))
        self.output = dirName

    @pyqtSlot()
    def compute(self):
        fileExist = path.isfile(self.inFile)
        dirExist = path.isdir(self.output)
        if fileExist and dirExist:
            tok = Tokenization(self.inFile, self.output)
            tok.run()
            QMessageBox.information(self, " ", lang[self.lang]["successful"])
        else:
            QMessageBox.warning(self, " ", lang[self.lang]["fail"])
