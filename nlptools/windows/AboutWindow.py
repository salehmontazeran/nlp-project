# from PyQt5.QtGui import Qwid
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont, QPainter, QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QSizePolicy,
                             QVBoxLayout, QWidget)

from .BaseWindow import BaseWindow
from .MainWindows import MainWindow


class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)


class AboutWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        # self.width = 500
        # self.height = 300
        self.pixmap = QPixmap('wall.jpg')
        self.title = self.title + ' - About'
        self.init()
        self.show()

    def init(self):
        # badicInit inherit from BaseWindow
        self.basicInit()
        self.setup()

    def setup(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # okBtn = QPushButton("OK", self)
        # okBtn.clicked.connect(self.on_click)
        labelImage = Label(self)
        labelImage.setPixmap(self.pixmap)

        myFont = QFont("Calibri")
        myFont.setPointSize(16)

        self.faPush = QPushButton("فارسی", self)
        self.faPush.setFont(myFont)
        self.faPush.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.enPush = QPushButton("English", self)
        self.enPush.setFont(myFont)
        self.enPush.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.faPush.clicked.connect(self.on_clickfa)
        self.enPush.clicked.connect(self.on_clicken)
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.faPush)
        hLayout.addWidget(self.enPush)

        layout = QVBoxLayout()
        layout.addWidget(labelImage, 11)
        layout.addLayout(hLayout, 1)

        wid.setLayout(layout)

    @pyqtSlot()
    def on_clickfa(self):
        self.mw = MainWindow("fa")
        self.close()

    @pyqtSlot()
    def on_clicken(self):
        self.mw = MainWindow("en")
        self.close()
