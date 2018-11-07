# -*- coding: utf-8 -*-
import sys
import queue
import re

from PyQt5 import QtWidgets,QtCore

from DataSet.datasetpage import Ui_MainWindow
import protocol


class Ui_DataSet(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,sendQuene,parent=None):
        super(Ui_DataSet, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.items = []      # data items
        self.loadConfig()       # read config file to initial the treeViewWidget
        self.sq = sendQuene  # data queue using to store send data
        self.setSingleMode()
        self.label_log.setText("")
        self.loadButton.clicked.connect(self.loadusrconfig)
        self.loadButton_self.clicked.connect(self.loadusrconfig_self)
        self.sendButton.clicked.connect(self.queneAdd)

    def setSingleMode(self):
        self.motoA.setVisible(False)
        self.motoB.setVisible(False)
        self.motoC.setVisible(False)
        self.motoD.setVisible(False)

    def queneAdd(self):
        self.label_log.setText("发送中")
        for i in range(len(self.items)):
            if(self.JudgeValidator(self.items[i].text(1))):
                if (self.motoA.isChecked()):
                    self.sq.put(protocol.de_convert(['out', 'Motor_A', i+1, float(self.items[i].text(1))]))
                if (self.motoB.isChecked()):
                    self.sq.put(protocol.de_convert(['out', 'Motor_B', i+1, float(self.items[i].text(1))]))
                if (self.motoC.isChecked()):
                    self.sq.put(protocol.de_convert(['out', 'Motor_C', i+1, float(self.items[i].text(1))]))
                if (self.motoD.isChecked()):
                    self.sq.put(protocol.de_convert(['out', 'Motor_D', i+1, float(self.items[i].text(1))]))
                self.label_log.setText("请选择电机")
                if (self.motoA.isChecked() | self.motoB.isChecked() | self.motoC.isChecked() | self.motoD.isChecked()):
                    self.label_log.setText("发送成功")

    def JudgeValidator(self,data):
        regInt = '^[-+]?[1-9]\d*$'  # 不接受09这样的为整数
        regFloat = '^[-+]?0\.\d+$|^[-+]?[1-9]\d*\.\d+$'
        regIntOrFloat = regInt + '|' + regFloat  # 整数或小数
        patternIntOrFloat = re.compile(regIntOrFloat)  # 创建pattern对象，以便后续可以复用

        if patternIntOrFloat.search(data):
            return True
        else:
            return False

    def loadusrconfig(self):
        myPath = QtWidgets.QFileDialog.getOpenFileName(self,
                                                       "选取配置文件，取消为默认配置",
                                                       "",
                                                       "Text Files (*.txt)")
        if myPath[0]:
            filepath = myPath[0]
        else:
            filepath = "userconfig\\usrdataset.txt"

        try:
            with open(filepath, 'r') as fs:
                i = 0
                for line in fs:
                    self.items[i].setText(1, line.strip('\n'))
                    i += 1
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "usrconfig file warning!",
                                              "设置和参数等个数的value")
            print(e)

    def loadusrconfig_self(self):
        filepath = "userconfig\\usrdataset.txt"
        try:
            with open(filepath, 'r') as fs:
                i = 0
                for line in fs:
                    self.items[i].setText(1, line.strip('\n'))
                    i += 1
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "usrconfig file warning!",
                                              "请在安装目录下设置config文件（sysconfig\dataset.config）并设置和参数等个数的value")
            print(e)

    def loadConfig(self):
        myPath = "sysconfig\\dataset.config"
        self.dataTable.clear()
        '''
        set 2 columns
        set the 'Value' list changeable
        self.dataTable.setColumnCount(2)
        self.dataTable.setHeaderLabels(['Parameter', 'Value'])
        '''
        try:
            with open(myPath, 'r') as fs:
                for line in fs:
                    item = QtWidgets.QTreeWidgetItem(self.dataTable)
                    self.dataTable.openPersistentEditor(item, 1)
                    item.setText(0, line.strip('\n'))
                    self.items.append(item)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "config file warning!", "请在安装目录下设置config文件（sysconfig\dataset.config）")
            print(e)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    q = queue.Queue()
    ds = Ui_DataSet(q)
    ds.show()
    app.exit(app.exec_())