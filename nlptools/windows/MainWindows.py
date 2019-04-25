from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QAction

from languages.lang import lang

from .BaseWindow import BaseWindow
from .RemoveWindow import RemoveWindow
from .SpellWindow import SpellWindow
# from .POSWindow import POSWindow
from .TokenizationWindow import TokenizationWindow
from .TopicWindow import TopicWindow
from .WordnetWindow import WordnetWindow

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
        myFont = QFont("Calibri")
        myFont.setPointSize(16)

        menu = self.menuBar()
        menu.setFont(myFont)
        tokenMenu = menu.addMenu(lang[self.la]["token"])
        spellMenu = menu.addMenu(lang[self.la]["spell"])
        removeMenu = menu.addMenu(lang[self.la]["remove"])
        posMenu = menu.addMenu(lang[self.la]["pos"])
        topicMenu = menu.addMenu(lang[self.la]["topic"])
        wsMenu = menu.addMenu(lang[self.la]["ws"])
        # helpMenu = menu.addMenu("Help")
        tokenMenu.addAction(self.makeTokenizationBtn())
        posMenu.addAction(self.makePOSBtn())
        spellMenu.addAction(self.makeSpellBtn())
        removeMenu.addAction(self.makeRemoveBtn())
        topicMenu.addAction(self.makeTopicBtn())
        wsMenu.addAction(self.makeWsBtn())

    def makeTokenizationBtn(self):
        def on_click():
            self.tw = TokenizationWindow(self.la)

        aboutBtn = QAction(QIcon(), lang[self.la]["token"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn

    def makePOSBtn(self):
        def on_click():
            # self.tw = POSWindow(self.la)
            pass

        aboutBtn = QAction(QIcon(), lang[self.la]["pos"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn

    def makeSpellBtn(self):
        def on_click():
            self.sc = SpellWindow(self.la)
            self.sc.correct()

        aboutBtn = QAction(QIcon(), lang[self.la]["spell"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn

    def makeTopicBtn(self):
        def on_click():
            self.tw = TopicWindow(self.la)

        aboutBtn = QAction(QIcon(), lang[self.la]["topic"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn

    def makeWsBtn(self):
        def on_click():
            self.ww = WordnetWindow(self.la)

        aboutBtn = QAction(QIcon(), lang[self.la]["ws"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn

    def makeRemoveBtn(self):
        def on_click():
            self.rw = RemoveWindow(self.la)
            self.rw.remove()

        aboutBtn = QAction(QIcon(), lang[self.la]["remove"], self)
        aboutBtn.triggered.connect(on_click)

        return aboutBtn
