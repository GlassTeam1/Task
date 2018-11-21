# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from queue import Queue

from PyQt5.QtCore import QPoint, QRect, QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
from producer import *
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import startListen

class Ui_MainWindow(object):
    def __init__(self):
        self.queue = Queue(maxsize=10)
        self.producer = Producer('Pro.', self.queue)
        self.consumer = Consumer('Con.', self.queue)
        self.datas = []
        self.datas1 = []
        self.datas2 = []
        self.datas3 = []
        self.datas_x = []
        self.datas_y = []
        self.datas_z = []
        self.datas_fengya = []
        self.datas_dianzu = []
        self.datas_wendu = []

        # 设置数据集的最大容量
        self.maxLength = 400
        self.pointDistance = 5  # 每点之间的间隔
        # 设置更新时间间隔
        self.updateInterval = 500  # 毫秒

        # 设置宽度
        self.boxWidth = 500


        # Enable antialiasing for prettier plots  防止反走样
        pg.setConfigOptions(antialias=True)

    def TimeAction(self):
        '''
                对于不同的图表，数据来源不同，可以采用多线程的方式;
                如果所有数据的来源一致，则：
                可将consumer.getData()的返回结果封装为对象
                '''
        self.data_queue = self.consumer.getData()  # array

        '''
        对于结果数据的展示可以按照这样的思路进行：
        将上面的数据全部得到之后，再调用MATLAB算法，将计算结果进行显示（看效率，如果效率太差则另想办法）
        或者
        将获取的数据存到数据库，另外启动一个线程专门对数据进行批处理，将计算结果再重新存入数据库中        
        '''

        # 头插法不断插入到总datas里
        self.datas.insert(0, self.data_queue[9])  # 结果数据
        self.datas1.insert(0, self.data_queue[6])  # 转角x
        self.datas2.insert(0, self.data_queue[7])  # 转角y
        self.datas3.insert(0, self.data_queue[8])  # 转角z

        self.datas_x.insert(0, self.data_queue[0])  # 加速度x
        self.datas_y.insert(0, self.data_queue[1])  # 加速度y
        self.datas_z.insert(0, self.data_queue[2])  # 加速度z
        self.datas_fengya.insert(0, self.data_queue[5])  # 风压
        self.datas_dianzu.insert(0, self.data_queue[3])  # 电阻应力
        self.datas_wendu.insert(0, self.data_queue[4])  # 温度
        # data = Data().data
        # 头插法不断插入到总datas里
        # datas.insert(0,datas)
        # 更新表1数据
        # print(datas)
        # print(datas1)
        # p1.plot(x=list(range(0,10,1)),y=datas[-10:])
        self.curve.setData(self.datas[:11])
        # p2.update()
        # clear每次都清空上一次画出来的图（是清除所有的plot)
        # 为什么不用setData，因为setData不能画多条线
        self.p2.setXRange(0, 10)
        if len(self.datas) == 1:
            self.p2.plot(self.datas1[:11], clear=True, pen='y', symbolBrush=(0, 255, 0), name='转角x')
            self.p2.plot(self.datas2[:11], pen='g', symbolBrush=(0, 255, 0), name='转角y')
            self.p2.plot(self.datas3[:11], pen='r', symbolBrush=(0, 255, 0), name='转角z')
        else:
            self.p2.plot(self.datas1[:11], clear=True, pen='y', symbolBrush=(0, 255, 0))
            self.p2.plot(self.datas2[:11], pen='g', symbolBrush=(0, 255, 0))
            self.p2.plot(self.datas3[:11], pen='r', symbolBrush=(0, 255, 0))
        # curve2.setData(datas1[:11])
        self.curve3.setData(self.datas_x[:11])
        self.curve4.setData(self.datas_y[:11])
        self.curve5.setData(self.datas_z[:11])
        self.curve6.setData(self.datas_fengya[:11])
        self.curve7.setData(self.datas_dianzu[:11])
        self.curve8.setData(self.datas_wendu[:11])
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1169, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")



        #开始画图***********************************************************************************************
        #第一列画图开始
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        #图一共有两列，这是第一列第一行的图
        self.graphicsView_1 = pg.GraphicsView(self.groupBox)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.l1 = pg.GraphicsLayout()
        self.graphicsView_1.setCentralItem(self.l1)
        self.graphicsView_1.show()
        self.p1 = self.l1.addPlot(title="结果")
        self.p1.enableAutoRange('xy', True)
        self.p1.setXRange(0, 10)
        self.curve = self.p1.plot(pen='y', symbolBrush=(0, 255, 0))
        self.gridLayout_2.addWidget(self.graphicsView_1, 0, 0, 1, 1)

        #第一列第二行的图
        self.graphicsView_3 = pg.GraphicsView(self.groupBox)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.l3=pg.GraphicsLayout()
        self.graphicsView_3.setCentralItem(self.l3)
        self.graphicsView_3.show()
        self.p3 = self.l3.addPlot(title='加速度x')
        self.curve3 = self.p3.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p3.enableAutoRange('xy', True)
        self.p3.setXRange(0, 10)
        self.gridLayout_2.addWidget(self.graphicsView_3, 1, 0, 1, 1)


        #第一列第三行的图
        self.graphicsView_5 = pg.GraphicsView(self.groupBox)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.l5 = pg.GraphicsLayout()
        self.graphicsView_5.setCentralItem(self.l5)
        self.graphicsView_5.show()
        self.p5 = self.l5.addPlot(title='加速度z')
        self.curve5 = self.p5.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p5.enableAutoRange('xy', True)
        self.p5.setXRange(0, 10)
        self.gridLayout_2.addWidget(self.graphicsView_5, 2, 0, 1, 1)


        #第一列第四行的图
        self.graphicsView_7 = pg.GraphicsView(self.groupBox)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.l7 = pg.GraphicsLayout()
        self.graphicsView_7.setCentralItem(self.l7)
        self.graphicsView_7.show()
        self.p7 = self.l7.addPlot(title='电阻')
        # symbolBrush用来设置点的颜色
        self.curve7 = self.p7.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p7.enableAutoRange('xy', True)
        self.p7.setXRange(0, 10)
        self.gridLayout_2.addWidget(self.graphicsView_7, 3, 0, 1, 1)

        #第一列结束
        self.horizontalLayout.addLayout(self.gridLayout_2)
        #第二列开始

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        #第二列第一行的图
        self.graphicsView_2 = pg.GraphicsView(self.groupBox)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.l2 = pg.GraphicsLayout()
        self.graphicsView_2.setCentralItem(self.l2)
        self.graphicsView_2.show()
        self.p2 = self.l2.addPlot(title="偏转角")
        self.p2.addLegend(offset=(0, 0))
        # curve2 = p2.plot(pen='y',symbolBrush=(0,255,0))
        self.p2.enableAutoRange('xy', True)
        self.gridLayout_3.addWidget(self.graphicsView_2, 0, 0, 1, 1)

        # 第二列第二行的图
        self.graphicsView_4 = pg.GraphicsView(self.groupBox)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.l4 = pg.GraphicsLayout()
        self.graphicsView_4.setCentralItem(self.l4)
        self.graphicsView_4.show()
        self.p4 = self.l4.addPlot(title='加速度y')
        self.curve4 = self.p4.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p4.enableAutoRange('xy', True)
        self.p4.setXRange(0, 10)
        self.gridLayout_3.addWidget(self.graphicsView_4, 1, 0, 1, 1)

        # 第二列第三行的图
        self.graphicsView_6 = pg.GraphicsView(self.groupBox)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.l6=pg.GraphicsLayout()
        self.graphicsView_6.setCentralItem(self.l6)
        self.graphicsView_6.show()
        self.p6 = self.l6.addPlot(title='风压')
        self.curve6 = self.p6.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p6.enableAutoRange('xy', True)
        self.p6.setXRange(0, 10)
        self.gridLayout_3.addWidget(self.graphicsView_6, 2, 0, 1, 1)

        # 第二列第四行的图
        self.graphicsView_8 = pg.GraphicsView(self.groupBox)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.l8=pg.GraphicsLayout()
        self.graphicsView_8.setCentralItem(self.l8)
        self.graphicsView_8.show()
        self.p8 = self.l8.addPlot(title='温度')
        self.curve8 = self.p8.plot(pen='y', symbolBrush=(0, 255, 0))
        self.p8.enableAutoRange('xy', True)
        self.p8.setXRange(0, 10)
        self.gridLayout_3.addWidget(self.graphicsView_8, 3, 0, 1, 1)
        #第二列画图结束
        self.horizontalLayout.addLayout(self.gridLayout_3)
        #画图结束！*************************************************************************************************************
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)

        # 动态加入下拉框空位
        self.comboBox_2.setObjectName("comboBox_2")
        for i in range(len(startListen.StartListen().serialPort)):
            self.comboBox_2.addItem("")

        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1169, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        # 非自动生成的代码***************************************************************************************************************

        self.timer = QTimer()
        # 触发器
        self.timer.timeout.connect(self.TimeAction)
        self.timer.setInterval(self.updateInterval)
        #self.timer.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BetaWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "View"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Selection"))
        self.pushButton.setText(_translate("MainWindow", "启动"))
        self.pushButton.clicked.connect(self.buttonClicked1)
        self.comboBox_3.setItemText(0, _translate("MainWindow", "38400"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "19200"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "9600"))
        self.label.setText(_translate("MainWindow", "传感器"))
        self.label_4.setText(_translate("MainWindow", "终止位："))
        self.label_2.setText(_translate("MainWindow", "端口选择"))
        self.label_3.setText(_translate("MainWindow", "波特率："))
        self.comboBox.setItemText(0, _translate("MainWindow", "com1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "com2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "com3"))

        # 动态添加下拉框内容
        for n,i in enumerate(startListen.StartListen().serialPort):
            self.comboBox_2.setItemText(n, _translate("MainWindow", i))


        self.comboBox_5.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "数据位"))
        self.pushButton_3.setText(_translate("MainWindow", "暂停"))
        self.pushButton_3.clicked.connect(self.buttonClicked)
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
    def buttonClicked(self):
        self.timer.stop()
    def buttonClicked1(self):
        self.timer.start()

import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #开启生产者消费者线程 分别用于读取数据和存储数据
    ui.producer.start()
    ui.consumer.start()
    #计时器开始
    ui.timer.start()
    MainWindow.show()
    sys.exit(app.exec_())
