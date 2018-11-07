# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datasetpage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 673)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/MonitorIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 30, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.motoLayout = QtWidgets.QHBoxLayout()
        self.motoLayout.setContentsMargins(-1, 5, -1, -1)
        self.motoLayout.setObjectName("motoLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.motoLayout.addItem(spacerItem)
        self.motoA = QtWidgets.QCheckBox(self.centralwidget)
        self.motoA.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.motoA.setFont(font)
        self.motoA.setChecked(True)
        self.motoA.setObjectName("motoA")
        self.motoLayout.addWidget(self.motoA)
        self.motoB = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.motoB.setFont(font)
        self.motoB.setObjectName("motoB")
        self.motoLayout.addWidget(self.motoB)
        self.motoC = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.motoC.setFont(font)
        self.motoC.setObjectName("motoC")
        self.motoLayout.addWidget(self.motoC)
        self.motoD = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.motoD.setFont(font)
        self.motoD.setObjectName("motoD")
        self.motoLayout.addWidget(self.motoD)
        self.gridLayout.addLayout(self.motoLayout, 2, 0, 1, 1)
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setObjectName("label_log")
        self.gridLayout.addWidget(self.label_log, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setContentsMargins(-1, 5, -1, -1)
        self.buttonLayout.setObjectName("buttonLayout")
        self.loadButton_self = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.loadButton_self.setFont(font)
        self.loadButton_self.setObjectName("loadButton_self")
        self.buttonLayout.addWidget(self.loadButton_self)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.buttonLayout.addWidget(self.loadButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.buttonLayout.addWidget(self.sendButton)
        self.gridLayout.addLayout(self.buttonLayout, 3, 0, 1, 1)
        self.dataTable = QtWidgets.QTreeWidget(self.centralwidget)
        self.dataTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dataTable.setObjectName("dataTable")
        self.gridLayout.addWidget(self.dataTable, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "参数控制"))
        self.motoA.setText(_translate("MainWindow", "MOTO_A"))
        self.motoB.setText(_translate("MainWindow", "MOTO_B"))
        self.motoC.setText(_translate("MainWindow", "MOTO_C"))
        self.motoD.setText(_translate("MainWindow", "MOTO_D"))
        self.label_log.setText(_translate("MainWindow", "TextLabel"))
        self.loadButton_self.setText(_translate("MainWindow", "默认配置"))
        self.loadButton.setText(_translate("MainWindow", "自定配置"))
        self.sendButton.setText(_translate("MainWindow", "发送参数"))
        self.dataTable.headerItem().setText(0, _translate("MainWindow", "Parameter"))
        self.dataTable.headerItem().setText(1, _translate("MainWindow", "Value"))

import Resource.Resource