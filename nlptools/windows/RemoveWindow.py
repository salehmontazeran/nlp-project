from collections import defaultdict

from PyQt5.QtWidgets import QMessageBox

from languages.lang import lang

from .BaseWindow import BaseWindow


class RemoveWindow(BaseWindow):
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

    def remove(self):
        inFile = "corpus/test.txt"
        outFile = "corpus/external/out.txt"

        ext = defaultdict(lambda: False)
        with open("corpus/ext.txt", "r", encoding="utf8") as i:
            line = i.readline()
            while line:
                line = line.strip()
                words = line.split()
                if len(words) == 1:
                    word = words[0].strip()
                    ext[word] = True
                line = i.readline()

        with open(outFile, "w", encoding="utf8") as o:
            with open(inFile, "r", encoding="utf8") as i:
                line = i.readline()
                while line:
                    out = []
                    line = line.strip()
                    words = line.split()
                    for w in words:
                        if ext[w] is False:
                            out.append(w)
                    outLine = " ".join(out)
                    o.write(outLine)
                    o.write("\n")
                    line = i.readline()
        self.showDone()

    def showDone(self):
        QMessageBox.information(self, " ", "done")
