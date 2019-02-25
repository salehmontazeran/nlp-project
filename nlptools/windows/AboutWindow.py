# from PyQt5.QtGui import Qwid
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from .BaseWindow import BaseWindow
from .MainWindows import MainWindow


class AboutWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 300
        self.pixmap = QPixmap('about.png')
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
        labelImage = QLabel(self)
        labelImage.setPixmap(self.pixmap)

        self.faPush = QPushButton("فارسی", self)
        self.enPush = QPushButton("English", self)
        self.faPush.clicked.connect(self.on_clickfa)
        self.enPush.clicked.connect(self.on_clicken)
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.faPush)
        hLayout.addWidget(self.enPush)

        layout = QVBoxLayout()
        layout.addWidget(labelImage)
        layout.addLayout(hLayout)

        wid.setLayout(layout)

    @pyqtSlot()
    def on_clickfa(self):
        self.mw = MainWindow("fa")
        self.close()

    @pyqtSlot()
    def on_clicken(self):
        self.mw = MainWindow("en")
        self.close()
