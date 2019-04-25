from PyQt5.QtWidgets import QMessageBox

from languages.lang import lang
from nlptools.kernels.spellcorrect import correctSentences

from .BaseWindow import BaseWindow


class SpellWindow(BaseWindow):
    def __init__(self, l):
        super().__init__(l)
        self.lang = l
        self.title = self.title + ' - ' + lang[l]["spell"]
        # self.width = self.width / 2
        # self.height = self.height / 2
        self.inFile = ""
        self.output = ""
        # self.basicInit()
        # self.setup()
        # self.show()

    def correct(self):
        inFile = "corpus/test.txt"
        outFile = "corpus/spell/out.txt"

        with open(outFile, "w", encoding="utf8") as o:
            with open(inFile, "r", encoding="utf8") as i:
                line = i.readline()
                while line:
                    line = line.strip()
                    t = correctSentences(line)
                    o.write(t)
                    o.write('\n')
                    line = i.readline()
        self.showDone()

    def showDone(self):
        QMessageBox.information(self, " ", "done")
