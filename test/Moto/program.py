import binascii
import re
import sys
import threading
import queue
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer

from Moto.DataSet.datasetWapper import Ui_DataSet
from Moto.MatplotlibShow.datamonitorWrapper import Ui_DataMonitor
from Moto.mainpage import Ui_MainWindow
import Moto.protocol as protocol


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setupvar()
        self.connectElement()

    '''设置指示灯'''
    def setlight(self,state):
        if state:
            self.label_4.setPixmap(QtGui.QPixmap(":/img/green.png"))
        else:
            self.label_4.setPixmap(QtGui.QPixmap(":/img/red.png"))


    '''设置关键属性：串口，定时器，队列（发送），队列（接受）'''
    def setupvar(self):
        self.SendQuene = queue.Queue()
        self.RevQuene = queue.Queue(maxsize=30000)
        self.ser = serial.Serial()
        self.sendtimer = QTimer()
        self.sendtimer.start(300)
        self.queneCheckTimer = QTimer()
        self.queneCheckTimer.start(1000)

    def connectElement(self):
        self.sendtimer.timeout.connect(self.timer_send)
        self.queneCheckTimer.timeout.connect(self.queneCheck)
        self.pushButton.clicked.connect(self.port_open)
        self.pushButton_2.clicked.connect(self.port_close)
        self.pushButton_6.clicked.connect(self.port_check)
        self.pushButton_3.clicked.connect(self.dataMonitor)
        self.pushButton_7.clicked.connect(self.sendbox)
        self.pushButton_8.clicked.connect(self.textBrowser.clear)
        self.pushButton_4.clicked.connect(self.dataSet)
        self.checkBox.stateChanged.connect(self.sendLineedit)

    '''发送button7 slot函数'''
    def sendbox(self):
        if(self.lineEdit_2.text() != ''):
            if self.checkBox.isChecked():
                self.send_data(self.lineEdit_2.text())
            else:
                self.send_data(self.lineEdit_2.text(),mode=False)

    '''设置checkbox hex状态改变的slot函数'''
    def sendLineedit(self):
        if(self.checkBox.isChecked()):
            self.lineEdit_2.setText('0x')
        else:
            self.lineEdit_2.clear()

    '''定时器slot函数，定时检测SendQuenen是否有数据需要发送'''
    def timer_send(self):
        while(True):
            if(not self.SendQuene.empty()):
                self.send_data(self.SendQuene.get())
            else:
                break


    '''串口部分'''
    def port_open(self):
        if(self.comboBox.currentText() and int(self.lineEdit.text()) ):
            self.port_close()
            try:
                self.ser.port = self.comboBox.currentText()
                self.ser.baudrate = int(self.lineEdit.text())
                if self.comboBox_2.currentText()=='Odd':
                    self.ser.parity = serial.PARITY_ODD
                elif self.comboBox_2.currentText()=='Even':
                    self.ser.parity = serial.PARITY_EVEN
                else:
                    self.ser.parity = serial.PARITY_NONE
                self.ser.open()
                if (self.ser.isOpen()):
                    self.textBrowser.setText("打开成功")
                    self.setlight(True)
                    self.t1 = threading.Thread(target=self.receive_data)
                    self.t1.setDaemon(True)
                    self.t1.start()
                else:
                    self.textBrowser.setText("打开失败")
            except:
                self.textBrowser.setText("串口异常")
        else:
            self.textBrowser.setText("错误COM口")

    def port_close(self):
        self.threadFalg = False
        self.ser.close()
        if(self.ser.is_open):
            self.textBrowser.append("关闭失败")
        else:
            self.pushButton.setEnabled(True)
            self.textBrowser.append("关闭成功")
            self.setlight(False)

    def send_data(self,data,mode=True):
        if (self.ser.isOpen()):
            if (mode):
                data = data[2:len(data)]
                if re.search('\A[0-9a-fA-F]+\Z',data):
                    if(len(data)%2!=0):
                        data = data + '0'
                    self.ser.write(binascii.a2b_hex(data))
                    self.textBrowser.append("send:0x"+data)
                else:
                    self.textBrowser.append("不符合十六进制")
            else:
                self.ser.write(data.encode('utf-8'))
                self.textBrowser.append("send:"+data)
            self.ser.flushOutput()
        else:
            self.textBrowser.append("发送失败")

    def receive_data(self):
        self.threadFalg = True
        print("The receive_data threading is start"+threading.current_thread().name)
        res_data = ''
        try:
            while (self.ser.isOpen()):
                size = self.ser.inWaiting()
                if size:
                    res_data = self.ser.read_all()
                    recdata_hexstring = '0x'+binascii.b2a_hex(res_data).decode()
                    recdata_hexstring = protocol.judgeRev(recdata_hexstring)
                    if recdata_hexstring:
                        for i in range(len(recdata_hexstring)):
                            if not self.RevQuene.full():
                                self.RevQuene.put(recdata_hexstring[i])
                                '''
                                ---show rev data---
                                if (self.checkBox_2.isChecked()):
                                    print('rev:'+recdata_hexstring[i])
                                else:
                                    print('rev:'+res_data.decode())
                                '''
                    else:
                        print('rev:无效数据:'+str(res_data))

                    self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                    self.ser.flushInput()
                if not self.threadFalg:
                    break
        except Exception as e:
            print(e)

    def port_check(self):
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox.addItem(port[0])
        if(len(Com_List) == 0):
            self.textBrowser.append("串口未连接")
            return False
        else:
            return True

    def queneCheck(self):
        if self.RevQuene.full():
            self.RevQuene.clear()

    '''主功能区域'''
    def dataMonitor(self):
        self.mainWindow1 = Ui_DataMonitor(self.RevQuene,self.SendQuene)
        self.mainWindow1.show()


    def dataSet(self):
        self.mainWindow2 = Ui_DataSet(self.SendQuene)
        self.mainWindow2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())