#@Time    :2018/10/30 19:29
from PyQt5 import QtCore,QtGui,QtWidgets
from myWindow.untitled import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.OPEN.clicked.connect(self.onWorldClicked())

    def onWorldClicked(self, remark):
        print(remark)
        self.Title.setText("Hello World")

    '''
     
    '''

import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
