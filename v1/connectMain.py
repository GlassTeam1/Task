# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import mainwindow2
import print
import sys


class Main(QMainWindow, mainwindow2.Ui_MainWindow2):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        #print("Main")


class Child(QMainWindow, print.Ui_MainWindow):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
        self.producer.start()
        self.consumer.start()
        self.timer.start()
        #print("Child")



    def OPEN(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ch = Child()
    main = Main()
    main.show()
    main.pushButton1.clicked.connect(ch.OPEN)
   # print("进入主程序")
    sys.exit(app.exec_())