#@Time    :2018/11/1 19:24
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

from button_connect.plot import Figure_Canvas
from button_connect.ui_start import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


        self.pushButton.clicked.connect(self.printGraph1)

        # 新建一个QTimer对象
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.start()
        # 信号连接到槽
        #self.timer.timeout.connect(self.printGraph1)

    def button(self,remark):
        print(remark)
        data = [[1, 2, 3, 4, 5, 6, 7, 8, 9,10], [23, 21, 32, 13, 3, 132, 13, 3, 1,13]]
        self.printGraph1(data)
    def printGraph1(self):
        data = [[1, 2, 3, 4, 5, 6, 7, 8, 9,10], [23, 21, 32, 13, 3, 132, 13, 3, 1,10]]
        dr = Figure_Canvas()  # 实例化一个FigureCanvas
        #dr.test(data)  # 画图
        dr.test2()
        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())