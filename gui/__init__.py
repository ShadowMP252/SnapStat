from gui.widgets import *
from gui.modules import *
from gui.mainWindow import TheMainWindow
import sys

def run():
    app = QApplication(sys.argv)
    window = TheMainWindow()
    sys.exit(app.exec())