import os

from PyQt5 import QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QPlainTextEdit

from languages.lang import lang

from ..kernels.pos import POS
from .BaseWindow import BaseWindow


class POSWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.lang = l
        self.title = self.title + ' - ' + lang[l]["pos"]
        # self.width = self.width / 2
        # self.height = self.height / 2
        self.inFile = ""
        self.output = ""
        self.basicInit()
        p = POS("corpus/fa.txt", "corpus/out/fa-tag.html")
        # p.posTaggerTXT()
        # self.setup2()
        p.posTaggerHTML()
        self.setup2()
        self.show()

    def setup(self):
        self.editor = QPlainTextEdit()
        self.setCentralWidget(self.editor)
        text = open("corpus/out/fa-tag.txt").read()
        self.editor.setPlainText(text)

    def setup2(self):
        self.web = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.web)
        # text = open("corpus/out/fa-tag.txt").read()
        # self.editor.setPlainText(text)
        self.web.load(QtCore.QUrl().fromLocalFile(
            os.path.split(
                os.path.abspath(__file__)
            )[0]+r'/../../corpus/out/fa-tag.html'
        ))
        print(os.path.split(
                os.path.abspath(__file__)
            )[0]+r'/../../corpus/out/fa-tag.html')
