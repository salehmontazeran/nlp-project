import sys
from PyQt5.QtWidgets import QApplication
# from nlptools.windows.MainWindows import MainWindow
from nlptools.windows.AboutWindow import AboutWindow


APP = QApplication(sys.argv)
am = AboutWindow()
sys.exit(APP.exec())
