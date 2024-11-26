import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow ,QLineEdit, QPushButton, QApplication,QVBoxLayout, QDialog
 
folderPath = "D:/tmp/Project_Rana/scripts/Rana/img"
sys.path.append(folderPath)

from Ui_main import Ui_MainWindow   

from PySide2.QtWidgets  import QApplication, QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)

        self.setWindowTitle("Rana GUI")

        

if (__name__ == '__main__'):

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()

    sys.exit(app.exec_())