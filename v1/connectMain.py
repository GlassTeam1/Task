# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import mainwindow2
import print
import sys

class Main(QMainWindow, mainwindow2.Ui_MainWindow2):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


class Child(QMainWindow, print.Ui_MainWindow10):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
        self.producer.start()
        self.consumer.start()
        self.timer.start()

    def OPEN(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main=Main()
    main.show()
    ch=Child()
    main.pushButton1.clicked.connect(ch.OPEN)
    sys.exit(app.exec_())