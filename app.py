import sys
from collections import defaultdict

from PyQt5.QtWidgets import QApplication

# from nlptools.kernels.spellcorrect import correctSentences
# from nlptools.kernels.wordnet import Wordnet
# from nlptools.kernels.spell import Spell
# from nlptools.kernels.engtopic import predict
from nlptools.windows.AboutWindow import AboutWindow

# from nlptools.windows.RemoveWindow import RemoveWindow

# t = Spell()
# print(predict(text))
# w = Wordnet()
# print(w.synsets("good"))

APP = QApplication(sys.argv)
am = AboutWindow()
sys.exit(APP.exec())


# print(correctSentences("شلام عزیژم"))

# with open("corpus/correct.txt", "w", encoding="utf8") as f:
#     f.write(correctSentences("شلام عزیژم خوبی"))

# rw = RemoveWindow("en")
# rw.remove()
