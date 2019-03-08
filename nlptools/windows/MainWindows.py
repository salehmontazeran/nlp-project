from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from languages.lang import lang

from .BaseWindow import BaseWindow
from .TokenizationWindow import TokenizationWindow

# from ..kernels.tokenization import ali


class MainWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.la = l
        self.title = self.title + ' - ' + lang[l]["main"]
        self.init()
        self.show()

    def init(self):
        # badicInit inherit from BaseWindow
        self.basicInit()
        self.menuInit()

    def menuInit(self):
        menu = self.menuBar()
        mainMenu = menu.addMenu(lang[self.la]["tools"])
        # helpMenu = menu.addMenu("Help")
        mainMenu.addAction(self.makeTokenizationBtn())

    def makeTokenizationBtn(self):
        def on_click():
            self.tw = TokenizationWindow(self.la)

        aboutBtn = QAction(QIcon(), lang[self.la]["token"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn
