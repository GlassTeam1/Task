import os
import queue
import threading
import time
from time import clock

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtCore import QTimer

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt

from MatplotlibShow.datamonitor import Ui_MainWindow
import protocol



class Ui_DataMonitor(QMainWindow,Ui_MainWindow):

    def __init__(self,RevQuene,SendQuene,parent=None):
        super(Ui_DataMonitor, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.sq = SendQuene
        self.rq = RevQuene
        self.setvar()
        self.dataView_init()
        self.connectElement()

    def setvar(self):
        # table item list 0--parameter 1--value
        self.itemListA = []
        self.itemListB = []
        self.itemListC = []
        self.itemListD = []

        #warning data form
        self.warning = [[True]*16,[True]*16,[True]*16,[True]*16]

        #set Form of the lineEdit text
        self.lineEdit_set1.setValidator(QDoubleValidator())
        self.lineEdit_set2.setValidator(QDoubleValidator())
        self.lineEdit.setValidator(QIntValidator())

        #采样间隔 defalt 10ms
        self.timebase = 10

        #采样点 坐标采用s point_x * timebase / 1000.0
        self.point_x = 0

        #show time clock and timeflag
        self.showtimer = QTimer()
        self.timeOn = False

        #set thread to receive data and process the revdata
        self.t_rev_end = False
        self.t_rev = threading.Thread(target=self.rev_queue)
        self.t_rev.setName("rev-data-thread")
        self.t_rev.start()


        # set timer to show the graph
        self.graphtimer = QTimer()

        # set figure
        self.figure = plt.figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.show()
        self.toolsbar = NavigationToolbar2QT(self.canvas, self)
        self.toolsbar.update()

        # set axes
        self.ax = self.figure.add_subplot(111)

        # set layout
        self.Layout_graph_2.addWidget(self.canvas)
        self.Layout_graph_2.addWidget(self.toolsbar)

        ##set test timer
        self.startime = clock()
        self.startime_pic = clock()

    def connectElement(self):
        self.PB_setdata.clicked.connect(self.dataset)
        self.PB_motostart.clicked.connect(self.motor_start)
        self.PB_motostop.clicked.connect(self.motor_stop)
        self.PB_start.clicked.connect(self.start_send)
        self.PB_stop.clicked.connect(self.stop_send)
        self.PB_reloadfile.clicked.connect(self.dataView_init)
        self.PB_cleargraph.clicked.connect(self.cleardata)
        self.PB_savefile.clicked.connect(self.savedata)
        self.comboBox_moto.currentIndexChanged.connect(self.warn_set)

    def dataView_init(self):
        myPath = "sysconfig\\monitor.config"
        self.dataTable.clear()
        self.itemListA = []
        self.itemListB = []
        self.itemListC = []
        self.itemListD = []
        # set Qtreewidget root points
        self.root_motoA = QtWidgets.QTreeWidgetItem(self.dataTable)
        self.root_motoB = QtWidgets.QTreeWidgetItem(self.dataTable)
        self.root_motoC = QtWidgets.QTreeWidgetItem(self.dataTable)
        self.root_motoD = QtWidgets.QTreeWidgetItem(self.dataTable)
        self.root_motoA.setText(0, "Motor_A")
        self.root_motoB.setText(0, "Motor_B")
        self.root_motoC.setText(0, "Motor_C")
        self.root_motoD.setText(0, "Motor_D")

        try:
            fs = open(myPath, 'r')
            for line in fs:
                itemA = QtWidgets.QTreeWidgetItem(self.root_motoA)
                itemA.setText(0, line.strip('\n'))
                itemA.setCheckState(0, QtCore.Qt.Unchecked)
                self.itemListA.append(itemA)

                itemB = QtWidgets.QTreeWidgetItem(self.root_motoB)
                itemB.setText(0, line.strip('\n'))
                itemB.setCheckState(0, QtCore.Qt.Unchecked)
                self.itemListB.append(itemB)

                itemC = QtWidgets.QTreeWidgetItem(self.root_motoC)
                itemC.setText(0, line.strip('\n'))
                itemC.setCheckState(0, QtCore.Qt.Unchecked)
                self.itemListC.append(itemC)

                itemD = QtWidgets.QTreeWidgetItem(self.root_motoD)
                itemD.setText(0, line.strip('\n'))
                itemD.setCheckState(0, QtCore.Qt.Unchecked)
                self.itemListD.append(itemD)

        except Exception as e:
            QMessageBox.information(self, "config file warning!", "请在安装目录下设置config文件（sysconfig\monitor.config）")
            print(e)

        # set single mode
        self.setSingleMode()

    def rev_queue(self):
        while(not self.t_rev_end):
            if (not self.rq.empty() and self.timeOn == True):
                res = protocol.convert(self.rq.get())
                try:
                    self.data_process(res)
                except IndexError as e:
                    print(e)
            else:
                time.sleep(0.005)

    def showtime(self):
        self.point_x += 1
        self.label_time.setText(str(self.point_x * self.timebase) + "ms")

    def data_process(self, res):
        # - Test Time -
        #print("start data_process at {0} ".format(self.startime))
        self.startime = clock()
        # - - - - - - -

        if (res):
            if (res[0] == 'out'):
                if (res[1] == 'Motor_A'):
                    self.itemListA[res[2]-1].setText(1,str(res[3]))
                    self.writefile("motoA_"+str(res[2])+'.log',self.point_x*self.timebase/1000.0,res[3])
                elif (res[1] == 'Motor_B'):
                    self.itemListB[res[2]-1].setText(1, str(res[3]))
                    self.writefile("motoB_" + str(res[2]) + '.log', self.point_x * self.timebase/1000.0, res[3])
                elif (res[1] == 'Motor_C'):
                    self.itemListC[res[2]-1].setText(1, str(res[3]))
                    self.writefile("motoC_" + str(res[2]) + '.log', self.point_x * self.timebase/1000.0, res[3])
                else:
                    self.itemListD[res[2]-1].setText(1, str(res[3]))
                    self.writefile("motoD_" + str(res[2]) + '.log', self.point_x * self.timebase/1000.0, res[3])

                # - Test Time - write points time
                print("Write time: {0} ".format(clock() - self.startime))
                self.startime = clock()
                # - - - - - - -

            elif (res[0] == 'warning'):
                if (res[1] == 'Motor_A'):
                    self.warning[0][res[2]-1] = False
                elif (res[1] == 'Motor_B'):
                    self.warning[1][res[2]-1] = False
                elif (res[1] == 'Motor_C'):
                    self.warning[2][res[2]-1] = False
                else:
                    self.warning[3][res[2]-1] = False
                self.warn_set()

    def warn_set(self):
        # 判断显示电机的参数
        item = self.comboBox_moto.currentText()
        # 判断显示电机的参数
        if item == 'MotoA':
            for i in range(16):
                self.changeLight(i+1,self.warning[0][i])
        elif item == 'MotoB':
            for i in range(16):
                self.changeLight(i+1,self.warning[1][i])
        elif item == 'MotoC':
            for i in range(16):
                self.changeLight(i+1,self.warning[2][i])
        else:
            for i in range(16):
                self.changeLight(i+1,self.warning[3][i])

    '''开始和结束slot函数，对sq进行操作'''
    def start_send(self):
        self.sq.put(protocol.de_convert('start'))
        self.point_x = 0
        if self.lineEdit.text():
            self.timebase = int(self.lineEdit.text())
            self.sq.put(protocol.de_convert(['time', 'Motor_A', int(self.lineEdit.text())]))
        else:
            self.timebase = 10
            self.sq.put(protocol.de_convert(['time', 'Motor_A', 10]))

        #set show time and timeOn flag
        self.showtimer.start(self.timebase)
        self.showtimer.timeout.connect(self.showtime)
        self.timeOn = True

        for i in range(16):
            self.changeLight(i+1,True)

        #set timer for drawing picture
        self.graphtimer.start(100)
        self.graphtimer.timeout.connect(self.animate)

    def stop_send(self):
        self.sq.put(protocol.de_convert('stop'))

        self.showtimer.stop()
        self.timeOn = False
        self.graphtimer.stop()

        for i in range(16):
            self.changeLight(i+1,True)

    '''参数设置'''
    def dataset(self):
        # 判断显示电机的参数
        item = self.comboBox_moto.currentText()
        # 判断显示电机的参数
        if item == 'MotoA':
            moto = 'Motor_A'
        elif item == 'MotoB':
            moto = 'Motor_B'
        elif item == 'MotoC':
            moto = 'Motor_C'
        else:
            moto = 'Motor_D'
        #母线
        if self.lineEdit_set1.isModified():
            self.sq.put(protocol.de_convert(['out', moto, 17, float(self.lineEdit_set1.text())]))
        #转速
        if self.lineEdit_set2.isModified():
            self.sq.put(protocol.de_convert(['out', moto, 5, float(self.lineEdit_set2.text())]))

    '''启动电机，停止电机两个button的slot'''
    def motor_start(self):
        # 判断显示电机的参数
        item = self.comboBox_moto.currentText()
        # 判断显示电机的参数
        if item == 'MotoA':
            moto = 'Motor_A'
        elif item == 'MotoB':
            moto = 'Motor_B'
        elif item == 'MotoC':
            moto = 'Motor_C'
        else:
            moto = 'Motor_D'
        self.sq.put(protocol.de_convert(['begin',moto]))

    def motor_stop(self):
        # 判断显示电机的参数
        item = self.comboBox_moto.currentText()
        # 判断显示电机的参数
        if item == 'MotoA':
            moto = 'Motor_A'
        elif item == 'MotoB':
            moto = 'Motor_B'
        elif item == 'MotoC':
            moto = 'Motor_C'
        else:
            moto = 'Motor_D'
        self.sq.put(protocol.de_convert(['stop', moto]))

    ''' animate function'''
    def animate(self):
        self.ax.clear()

        # - Test Time_pic -
        #print("start animate function at {0} ".format(self.startime_pic))
        self.startime_pic = clock()
        # - - - - - - -

        try:
            listdir = os.listdir("syslog")
            for filename in listdir:
                filepath = os.path.join("syslog", filename)
                itemId = int(filename.split('.')[0].split('_')[1])-1
                moto = filename.split('.')[0].split('_')[0]
                if moto == "motoA":
                    flag = self.itemListA[itemId].checkState(0)
                elif moto == "motoB":
                    flag = self.itemListB[itemId].checkState(0)
                elif moto == "motoC":
                    flag = self.itemListC[itemId].checkState(0)
                elif moto == "motoD":
                    flag = self.itemListD[itemId].checkState(0)
                else:
                    flag = False
                if flag:
                    # - Test Time_pic - read points time
                    print("Reading points time: {0} ".format(clock() - self.startime_pic))
                    self.startime_pic = clock()
                    # - - - - - - -
                    try:
                        self.drawPic(filepath)
                        plt.legend()
                        self.ax.figure.canvas.draw()
                    except Exception as e:
                        print(e)
                    # - Test Time_pic - draw points time
                    print("Drawing points time: {0} ".format(clock() - self.startime_pic))
                    self.startime_pic = clock()
                    # - - - - - - -
        except:
            pass

    '''画图'''
    def drawPic(self,path):
        fs = open(path, "r")
        pullData = fs.read()
        dataList = pullData.split('\n')
        xList = []
        yList = []

        #cut the window
        if len(dataList) > 30000:
            fs.close()
            self.cutwindow(path)
            fs = open(path, "r")
            pullData = fs.read()
            dataList = pullData.split('\n')

        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(float(x))
                yList.append(float(y))
        itemId = int(os.path.basename(path).split('.')[0].split('_')[1])
        moto = os.path.basename(path).split('.')[0].split('_')[0]
        if moto == "motoA":
            legend = moto + "_" + self.itemListA[itemId-1].text(0)
        elif moto == "motoB":
            legend = moto + "_" + self.itemListB[itemId-1].text(0)
        elif moto == "motoC":
            legend = moto + "_" + self.itemListC[itemId-1].text(0)
        elif moto == "motoD":
            legend = moto + "_" + self.itemListD[itemId-1].text(0)
        else:
            legend = "none"
        self.ax.plot(xList, yList, label=legend)
        fs.close()

    '''清楚数据'''
    def cleardata(self):
        try:
            for item in os.listdir("syslog"):
                itemsrc = os.path.join("syslog", item)
                os.remove(itemsrc)
            self.ax.figure.canvas.draw()
        except:
            pass

    '''保存数据'''
    def savedata(self):
        myPath = QtWidgets.QFileDialog.getSaveFileName(self,
                                    "数据保存",
                                    "",
                                    "Text Files (*.csv)")
        with open(myPath[0],'a') as fs:
            try:
                listdir = os.listdir("syslog")
                for filename in listdir:
                    filepath = os.path.join("syslog", filename)
                    itemId = int(filename.split('.')[0].split('_')[1]) - 1
                    moto = filename.split('.')[0].split('_')[0]
                    if moto == "motoA":
                        title = moto + "_" + self.itemListA[itemId].text(0)
                    elif moto == "motoB":
                        title = moto + "_" + self.itemListB[itemId].text(0)
                    elif moto == "motoC":
                        title = moto + "_" + self.itemListC[itemId].text(0)
                    elif moto == "motoD":
                        title = moto + "_" + self.itemListD[itemId].text(0)
                    else:
                        title = ""
                    fs.writelines(title+",")
                    #提取数据
                    pullData = open(filepath, "r").read()
                    dataList = pullData.split('\n')
                    for eachLine in dataList:
                        if len(eachLine) > 1:
                            x,value = eachLine.split(',')
                            fs.write(str(value)+",")
                    fs.write("\n")
            except:
                pass

    '''关闭程序之前，删除syslog文件夹内容, timer停止'''
    def closeEvent(self, *args, **kwargs):
        try:
            self.t_rev_end = True
            for item in os.listdir("syslog"):
                itemsrc = os.path.join("syslog", item)
                os.remove(itemsrc)
            self.sendtimer.stop()
            self.graphtimer.stop()
        except:
            pass

    '''设置单电机模式'''
    def setSingleMode(self):
        self.comboBox_moto.setVisible(False)
        self.root_motoB.setHidden(True)
        self.root_motoC.setHidden(True)
        self.root_motoD.setHidden(True)

    '''
    function part
    '''
    def changeLight(self,num,state):
        if state:
            item = ":/icons/icons/green-led-on.png"
        else:
            item = ":/icons/icons/led-red-on.png"
        if num == 1:
            self.labelStatusFan1.setPixmap(QtGui.QPixmap(item))
        elif num == 2:
            self.labelStatusFan2.setPixmap(QtGui.QPixmap(item))
        elif num == 3:
            self.labelStatusFan3.setPixmap(QtGui.QPixmap(item))
        elif num == 4:
            self.labelStatusFan4.setPixmap(QtGui.QPixmap(item))
        elif num == 5:
            self.labelStatusFan5.setPixmap(QtGui.QPixmap(item))
        elif num == 6:
            self.labelStatusFan6.setPixmap(QtGui.QPixmap(item))
        elif num == 7:
            self.labelStatusFan7.setPixmap(QtGui.QPixmap(item))
        elif num == 8:
            self.labelStatusFan8.setPixmap(QtGui.QPixmap(item))
        elif num == 9:
            self.labelStatusFan9.setPixmap(QtGui.QPixmap(item))
        elif num == 10:
            self.labelStatusFan10.setPixmap(QtGui.QPixmap(item))
        elif num == 11:
            self.labelStatusFan11.setPixmap(QtGui.QPixmap(item))
        elif num == 12:
            self.labelStatusFan12.setPixmap(QtGui.QPixmap(item))
        elif num == 13:
            self.labelStatusFan13.setPixmap(QtGui.QPixmap(item))
        elif num == 14:
            self.labelStatusFan14.setPixmap(QtGui.QPixmap(item))
        elif num == 15:
            self.labelStatusFan15.setPixmap(QtGui.QPixmap(item))
        elif num == 16:
            self.labelStatusFan16.setPixmap(QtGui.QPixmap(item))
        else:
            pass

    def writefile(self,filename, t=0.0, value=0.0):
        try:
            with open('syslog\\' + filename,'a') as fs:
                fs.writelines(str(t)+"," + str(value) + "\n")
        except Exception as e:
            QMessageBox.information(self, "config file warning!", "请在安装目录下设置syslog文件夹")
            print(e)


    def cutwindow(self, path):
        with open(path, 'r') as fs:
            pullData = fs.read()
            dataList = pullData.split('\n')
        os.remove(path)
        with open(path, 'a') as fs:
            length = len(dataList)
            for i in range(length/2,length):
                fs.writelines(dataList[i])


#如果想测试需要修改sysconfig路径
if __name__ == '__main__':
    app = QApplication([])
    page = Ui_DataMonitor(queue.Queue(),queue.Queue())
    page.show()
    app.exit(app.exec_())

