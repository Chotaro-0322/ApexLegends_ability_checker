import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from photoview import Ui_MainWindow, GraphicsSceneForMainView

class Setup(QMainWindow):
    def __init__(self, parent=None):
        super(Setup, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Setup()
    window.show()
    sys.exit(app.exec_())

