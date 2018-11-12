from queue import Queue

from PyQt5.QtCore import QPoint, QRect, QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
from producer import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

'''
只能定义为全局变量
数据来源如果是多个，则还需要声明多个存储队列
'''
queue = Queue(maxsize=10)
producer = Producer('Pro.', queue)
consumer = Consumer('Con.', queue)

#下面这个类用来模拟获取数据
# class Data:
#     def __init__(self,queue):
#         self.data = np.random.randint(0,20)#随机生成一个0到20的数
#     def GetData(self):
#         return self.data
class Data:
    def __init__(self):
        self.data=np.random.randint(0,20)#随机生成一个0到20的数
    def GetData(self):
        return self.data

datas=[]
datas1=[]
datas2=[]
datas3=[]
datas_x=[]
datas_y=[]
datas_z=[]
datas_fengya=[]
datas_dianzu=[]
datas_wendu=[]

        #设置数据集的最大容量
maxLength = 400
pointDistance = 5  # 每点之间的间隔
        #设置更新时间间隔
updateInterval = 500#毫秒

        #设置宽度
boxWidth=500

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000, 800)
win.setWindowTitle('pyqtgraph example: Plotting')
# Enable antialiasing for prettier plots  防止反走样
pg.setConfigOptions(antialias=True)
p1 = win.addPlot(title="Updating plot")
# 颜色
curve = p1.plot(pen='y')
p1.enableAutoRange('xy', True)

def TimeAction():
    '''
            对于不同的图表，数据来源不同，可以采用多线程的方式;
            如果所有数据的来源一致，则：
            可将consumer.getData()的返回结果封装为对象
            '''
    data_queue = consumer.getData()  # array

    '''
    对于结果数据的展示可以按照这样的思路进行：
    将上面的数据全部得到之后，再调用MATLAB算法，将计算结果进行显示（看效率，如果效率太差则另想办法）
    或者
    将获取的数据存到数据库，另外启动一个线程专门对数据进行批处理，将计算结果再重新存入数据库中        
    '''

    # 头插法不断插入到总datas里
    datas.insert(0, data_queue[9])  # 结果数据
    datas1.insert(0, data_queue[6])  # 转角x
    datas2.insert(0, data_queue[7])  # 转角y
    datas3.insert(0, data_queue[8])  # 转角z

    datas_x.insert(0, data_queue[0])  # 加速度x
    datas_y.insert(0, data_queue[1])  # 加速度y
    datas_z.insert(0, data_queue[2])  # 加速度z
    datas_fengya.insert(0, data_queue[5])  # 风压
    datas_dianzu.insert(0, data_queue[3])  # 电阻应力
    datas_wendu.insert(0, data_queue[4])  # 温度
    #data = Data().data
    # 头插法不断插入到总datas里
    #datas.insert(0,data)
    #更新表1数据
    print(datas)
    #p1.plot(x=list(range(0,10,1)),y=datas[-10:])
    curve.setData(datas[:11])

    if len(datas) > maxLength:
        datas.pop(- 1)
timer=QTimer()
        #触发器
timer.timeout.connect(TimeAction)
timer.setInterval(updateInterval)
timer.start()


win.nextRow()


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
