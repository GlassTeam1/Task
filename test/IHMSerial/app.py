#! /Users/ewen/anaconda3/bin/python
# coding: utf-8


"""Common control interface."""


__author__ = "Ewen BRUN, Pierre HAON"
__email__ = "ewen.brun@ecam.fr"


import sys
import IHMSerial.ASerial
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


qtCreatorFile = "ui/mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class App(QMainWindow, Ui_MainWindow):
    """Mainwindow."""

    def __init__(self):
        """Init."""
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
