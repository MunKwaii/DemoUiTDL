import os
import sys

from ui_interface import *
from Custom_Widgets.Widgets import *
from PyQt6.QtWidgets import QApplication, QWidget

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #apply json style sheet
        loadJsonStyle(self, self.ui)
        
        self.show()
        
#execute app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())