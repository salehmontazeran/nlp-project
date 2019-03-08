from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from languages.lang import lang


class BaseWindow(QMainWindow):

    def __init__(self, la="en"):
        super().__init__()
        self.title = lang[la]["title"]
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.iconName = "icon.ico"

    def basicInit(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(self.width, self.height)
