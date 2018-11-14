from queue import Queue

from PyQt5.QtCore import QPoint, QRect, QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
from producer import *
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
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
p1 = win.addPlot(title="结果")

# 颜色
curve = p1.plot(pen='y',symbolBrush=(0,255,0))
p1.enableAutoRange('xy', True)
p1.setXRange(0,10)
#第二个图
p2 = win.addPlot(title="偏转角")
p2.addLegend(offset=(0,0))
#curve2 = p2.plot(pen='y',symbolBrush=(0,255,0))
p2.enableAutoRange('xy',True)
#换行
win.nextRow()
#第三个图
p3=win.addPlot(title='加速度x')
curve3=p3.plot(pen='y',symbolBrush=(0,255,0))
p3.enableAutoRange('xy',True)
p3.setXRange(0,10)
#第四个图
p4=win.addPlot(title='加速度y')
curve4=p4.plot(pen='y',symbolBrush=(0,255,0))
p4.enableAutoRange('xy',True)
p4.setXRange(0,10)
#换行
win.nextRow()
#第五个图
p5=win.addPlot(title='加速度z')
curve5=p5.plot(pen='y',symbolBrush=(0,255,0))
p5.enableAutoRange('xy',True)
p5.setXRange(0,10)
#第六个图
p6=win.addPlot(title='风压')
curve6=p6.plot(pen='y',symbolBrush=(0,255,0))
p6.enableAutoRange('xy',True)
p6.setXRange(0,10)
#换行
win.nextRow()
#第七个图
p7=win.addPlot(title='电阻')
#symbolBrush用来设置点的颜色
curve7=p7.plot(pen='y',symbolBrush=(0,255,0))
p7.enableAutoRange('xy',True)
p7.setXRange(0,10)
#第八个图
p8=win.addPlot(title='温度')
curve8=p8.plot(pen='y',symbolBrush=(0,255,0))
p8.enableAutoRange('xy',True)
p8.setXRange(0,10)
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
    #datas.insert(0,datas)
    #更新表1数据
    # print(datas)
    # print(datas1)
    #p1.plot(x=list(range(0,10,1)),y=datas[-10:])
    curve.setData(datas[:11])
    # p2.update()
    #clear每次都清空上一次画出来的图（是清除所有的plot)
    #为什么不用setData，因为setData不能画多条线
    p2.setXRange(0,10)
    if len(datas)==1:
        p2.plot(datas1[:11],clear=True,pen='y',symbolBrush=(0,255,0),name='转角x')
        p2.plot(datas2[:11],pen='g',symbolBrush=(0,255,0),name='转角y')
        p2.plot(datas3[:11],pen='r',symbolBrush=(0,255,0),name='转角z')
    else:
        p2.plot(datas1[:11], clear=True, pen='y', symbolBrush=(0, 255, 0))
        p2.plot(datas2[:11], pen='g', symbolBrush=(0, 255, 0))
        p2.plot(datas3[:11], pen='r', symbolBrush=(0, 255, 0))
    #curve2.setData(datas1[:11])
    curve3.setData(datas_x[:11])
    curve4.setData(datas_y[:11])
    curve5.setData(datas_z[:11])
    curve6.setData(datas_fengya[:11])
    curve7.setData(datas_dianzu[:11])
    curve8.setData(datas_wendu[:11])

timer=QTimer()
        #触发器
timer.timeout.connect(TimeAction)
timer.setInterval(updateInterval)
timer.start()






if __name__ == '__main__':
    producer.start()
    consumer.start()
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
