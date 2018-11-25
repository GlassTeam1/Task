# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowTest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import producer

from PyQt5.QtCore import QDate
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=2, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self):
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # 0.1表示将Hogs那一块凸显出来
        self.axes.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)

class Ui_MainWindow2(object):
    # 只能传入radio，不能使用self.radioButton
    def radioF(self,radio,dateEdit,timeEdit):
        if(radio.isChecked()):
            self.dateEdit.setDisabled(True)
            self.timeEdit.setDisabled(True)
        else:
            self.dateEdit.setDisabled(False)
            self.timeEdit.setDisabled(False)

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(1093, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../study/pic/begin.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)

        # 默认选中实时检测
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda: self.radioF(self.radioButton,self.dateEdit,self.timeEdit))

        # connect(ui.radioButton, SIGNAL(toggled(bool)), this, SLOT(radioBtnSlot()));
        # connect(ui.radioButton_2, SIGNAL(toggled(bool)), this, SLOT(radioBtnSlot2()));
        # connect(ui.radioButton_3, SIGNAL(toggled(bool)), this, SLOT(radioBtnSlot3()));

        self.horizontalLayout_3.addWidget(self.radioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        # 设置为当前日期
        t = time.strftime("%Y-%m-%d")
        self.dateEdit.setDate(QDate.fromString(t, 'yyyy-MM-dd'))

        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit.setDisabled(True)
        self.timeEdit.setDisabled(True)

        self.horizontalLayout_2.addWidget(self.timeEdit)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setMinimumSize(QtCore.QSize(403, 383))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -103, 380, 843))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")


        self.pushButton1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton1.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton1.setObjectName("pushButton1")



        self.horizontalLayout_6.addWidget(self.pushButton1)

        self.pushButton2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton2.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton2.setObjectName("pushButton2")

        self.horizontalLayout_6.addWidget(self.pushButton2)

        self.pushButton3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton3.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton3.setObjectName("pushButton3")

        self.horizontalLayout_6.addWidget(self.pushButton3)

        self.pushButton4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton4.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton4.setObjectName("pushButton4")

        self.horizontalLayout_6.addWidget(self.pushButton4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.pushButton5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton5.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton5.setObjectName("pushButton5")
        self.horizontalLayout_7.addWidget(self.pushButton5)
        self.pushButton6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton6.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton6.setObjectName("pushButton6")
        self.horizontalLayout_7.addWidget(self.pushButton6)
        self.pushButton7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton7.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton7.setObjectName("pushButton7")
        self.horizontalLayout_7.addWidget(self.pushButton7)
        self.pushButton8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton8.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton8.setObjectName("pushButton8")
        self.horizontalLayout_7.addWidget(self.pushButton8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton9.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton9.setObjectName("pushButton9")
        self.horizontalLayout_9.addWidget(self.pushButton9)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_9.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_9.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_16.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_9.addWidget(self.pushButton_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_13.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_13.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_31.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_13.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_32.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_13.addWidget(self.pushButton_32)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_10.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_18.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_10.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_10.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_20.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_10.addWidget(self.pushButton_20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_12.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_12.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_12.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_12.addWidget(self.pushButton_28)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_21.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_11.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_22.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_11.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_23.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_11.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_11.addWidget(self.pushButton_24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_45 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_45.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_45.setObjectName("pushButton_45")
        self.horizontalLayout_17.addWidget(self.pushButton_45)
        self.pushButton_46 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_46.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_46.setObjectName("pushButton_46")
        self.horizontalLayout_17.addWidget(self.pushButton_46)
        self.pushButton_47 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_47.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_47.setObjectName("pushButton_47")
        self.horizontalLayout_17.addWidget(self.pushButton_47)
        self.pushButton_48 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_48.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_48.setObjectName("pushButton_48")
        self.horizontalLayout_17.addWidget(self.pushButton_48)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_33 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_33.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_14.addWidget(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_34.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_14.addWidget(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_35.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_14.addWidget(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_36.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_14.addWidget(self.pushButton_36)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_41 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_41.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_41.setObjectName("pushButton_41")
        self.horizontalLayout_16.addWidget(self.pushButton_41)
        self.pushButton_42 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_42.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayout_16.addWidget(self.pushButton_42)
        self.pushButton_43 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_43.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_43.setObjectName("pushButton_43")
        self.horizontalLayout_16.addWidget(self.pushButton_43)
        self.pushButton_44 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_44.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_44.setObjectName("pushButton_44")
        self.horizontalLayout_16.addWidget(self.pushButton_44)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_37 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_37.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout_15.addWidget(self.pushButton_37)
        self.pushButton_38 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_38.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout_15.addWidget(self.pushButton_38)
        self.pushButton_39 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_39.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_39.setObjectName("pushButton_39")
        self.horizontalLayout_15.addWidget(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_40.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_15.addWidget(self.pushButton_40)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 400))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setMinimumSize(QtCore.QSize(260, 200))
        self.graphicsView.setMaximumSize(QtCore.QSize(400, 400))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_5.addWidget(self.graphicsView)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        # 根据传感器数据改变按钮颜色
        time.sleep(1)
        inseart = producer.R
        print("窗体读入数据库数据")
        print('flag',inseart)
        dc = {}
        if inseart[0][-2]>0.2:
            dc[self.pushButton1]='red'
        else:
            dc[self.pushButton1]='green'
        dc[self.pushButton2]='green'
        dc[self.pushButton3]='red'
        dc[self.pushButton4]='green'
        dc[self.pushButton5]='green'
        dc[self.pushButton6] = 'green'
        dc[self.pushButton7] = 'green'
        dc[self.pushButton8] = 'green'
        for key,value in dc.items():
            if value=='green':
                key.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                key.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.gridLayoutWidget = QtWidgets.QWidget()
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 10, 20))  # 定义gridLayout控件的大小和位置，4个数字分别为左边坐标，上边坐标，长，宽
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)  # 在gridLayoutWidget 上创建一个网格Layout，注意以gridLayoutWidget为参
        self.gridLayout_2.setObjectName("gridLayout_2")
        # ===通过graphicview来显示图形
        self.graphicview = QtWidgets.QGraphicsView(
            self.gridLayoutWidget)  # 第一步，创建一个QGraphicsView，注意同样以gridLayoutWidget为参
        self.graphicview.setObjectName("graphicview")
        self.gridLayout_2.addWidget(self.graphicview, 0, 0)
        # 第二步，将该QGraphicsView放入Layout中

        dr = Figure_Canvas()
        # 实例化一个FigureCanvas
        dr.test()  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!


        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "主界面"))
        self.groupBox_3.setTitle(_translate("MainWindow2", "软件信息"))
        self.label_2.setText(_translate("MainWindow2", "玻璃状态监测系统"))
        self.groupBox.setTitle(_translate("MainWindow2", "玻璃状态展示"))
        self.radioButton_2.setText(_translate("MainWindow2", "历史记录"))
        self.radioButton.setText(_translate("MainWindow2", "实时监测"))
        self.pushButton1.setText(_translate("MainWindow2", "玻璃1"))
        self.pushButton2.setText(_translate("MainWindow2", "玻璃2"))
        self.pushButton3.setText(_translate("MainWindow2", "玻璃3"))
        self.pushButton4.setText(_translate("MainWindow2", "玻璃4"))
        self.pushButton5.setText(_translate("MainWindow2", "玻璃5"))
        self.pushButton6.setText(_translate("MainWindow2", "玻璃6"))
        self.pushButton7.setText(_translate("MainWindow2", "玻璃7"))
        self.pushButton8.setText(_translate("MainWindow2", "玻璃8"))
        self.pushButton9.setText(_translate("MainWindow2", "玻璃9"))
        self.groupBox_2.setTitle(_translate("MainWindow2", "状态统计图"))



