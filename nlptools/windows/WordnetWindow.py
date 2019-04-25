from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                             QTextEdit, QVBoxLayout, QWidget)

from languages.lang import lang
from nlptools.kernels.wordnet import Wordnet

from .BaseWindow import BaseWindow


class WordnetWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.lang = l
        self.title = self.title + ' - ' + lang[l]["topic"]

        self.basicInit()
        self.setup()
        self.show()

    def setup(self):
        myFont = QFont("Calibri")
        myFont.setPointSize(14)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        firstLayout = QHBoxLayout()

        self.input = QTextEdit()
        self.input.setFont(myFont)
        self.go = QPushButton(lang[self.lang]["go"], self)
        self.go.clicked.connect(self.goslot)
        self.go.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.go.setFont(myFont)
        firstLayout.addWidget(self.input, 5)
        firstLayout.addWidget(self.go, 1)

        secondLayout = QVBoxLayout()
        self.syn = QTextEdit()
        self.syn.setFont(myFont)
        self.syn.setDisabled(True)

        self.ant = QTextEdit()
        self.ant.setFont(myFont)
        self.ant.setDisabled(True)
        secondLayout.addLayout(firstLayout)
        secondLayout.addStretch()
        synl = QLabel(self)
        synl.setText(lang[self.lang]["syn"])
        synl.setFont(myFont)
        secondLayout.addWidget(synl)
        secondLayout.addWidget(self.syn)
        antl = QLabel(self)
        antl.setText(lang[self.lang]["ant"])
        antl.setFont(myFont)
        secondLayout.addWidget(antl)
        secondLayout.addWidget(self.ant)

        wid.setLayout(secondLayout)

    @pyqtSlot()
    def goslot(self):
        w = Wordnet()
        res = w.s(self.input.toPlainText())
        s = ', '.join(res[0])
        a = ', '.join(res[1])
        self.syn.setText(s)
        self.ant.setText(a)
