# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import windowTest
import print
import sys


class Main(QMainWindow, windowTest.Ui_MainWindow2):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)



class Child(QMainWindow, print.Ui_MainWindow):
    def __init__(self):
        # super(Child, self).__init__()
        # self.setupUi(self)
        # self.producer.start()
        # self.consumer.start()
        # self.timer.start()
        # sys.exit(app.exec_())
        super(Child, self).__init__()
        self.setupUi(self)

        self.producer.start()
        self.consumer.start()
        self.timer.start()

    def OPEN(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    ch = Child()
    main.show()
    main.pushButton1.clicked.connect(ch.OPEN)
    sys.exit(app.exec_())