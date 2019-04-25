from PyQt5 import QtGui, QtWidgets

from languages.lang import lang


class BaseWindow(QtWidgets.QMainWindow):

    def __init__(self, la="en"):
        super().__init__()
        self.title = lang[la]["title"]
        self.screen = QtWidgets.QDesktopWidget()
        self.top = 0
        self.left = 0
        self.width = self.screen.width()
        self.height = self.screen.height()
        self.iconName = "icon.ico"

    def basicInit(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        # self.setGeometry(self.top, self.left, self.width, self.height)
        self.showMaximized()
        # self.setFixedSize(self.width, self.height)
