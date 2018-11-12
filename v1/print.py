#@Time    :2018/11/10 14:10
from queue import Queue

from PyQt5.QtCore import QPoint, QRect, QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
from producer import *

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

class Demo(QWidget):
    def __init__(self,parent,consumer):
        QWidget.__init__(self, parent)
        self.timer=QTimer()
        #触发器
        self.timer.timeout.connect(self.TimeAction)
        self.datas=[]
        self.datas1=[]
        self.datas2=[]
        self.datas3=[]
        self.datas_x=[]
        self.datas_y=[]
        self.datas_z=[]
        self.datas_fengya=[]
        self.datas_dianzu=[]
        self.datas_wendu=[]

        #设置数据集的最大容量
        self.maxLength = 400
        self.pointDistance = 5  # 每点之间的间隔
        #设置更新时间间隔
        self.updateInterval = 500#毫秒
        self.timer.setInterval(self.updateInterval)
        #设置宽度
        self.boxWidth=500
        self.timer.start()
    def TimeAction(self):
        '''
        对于不同的图表，数据来源不同，可以采用多线程的方式;
        如果所有数据的来源一致，则：
        可将consumer.getData()的返回结果封装为对象
        '''
        data_queue = consumer.getData() #array


        '''
        对于结果数据的展示可以按照这样的思路进行：
        将上面的数据全部得到之后，再调用MATLAB算法，将计算结果进行显示（看效率，如果效率太差则另想办法）
        或者
        将获取的数据存到数据库，另外启动一个线程专门对数据进行批处理，将计算结果再重新存入数据库中        
        '''


        #头插法不断插入到总datas里
        self.datas.insert(0,data_queue[9]) #结果数据
        self.datas1.insert(0,data_queue[6]) #转角x
        self.datas2.insert(0,data_queue[7]) #转角y
        self.datas3.insert(0,data_queue[8]) #转角z

        self.datas_x.insert(0, data_queue[0])  # 加速度x
        self.datas_y.insert(0, data_queue[1])  # 加速度y
        self.datas_z.insert(0, data_queue[2])  # 加速度z
        self.datas_fengya.insert(0, data_queue[5])  # 风压
        self.datas_dianzu.insert(0, data_queue[3])  # 电阻应力
        self.datas_wendu.insert(0, data_queue[4])  # 温度

        if len(self.datas) > self.maxLength:
            #这个时候你从页面上看到的效果就是曲线一点点消失了。
            self.loads.pop(- 1)


        if self.isVisible():
            #更新画面  paintEvent(QPaintEvent*)函数是QWidget类中的虚函数，用于ui的绘制，会在多种情况下被其他函数自动调用，比如update()时。
            self.update()
    def paintEvent(self, event):
        #width, height = self.width(), self.height()

        polygon = QPolygon()
        for i,data in enumerate(self.datas):
            x = i * self.pointDistance
            y=160-data*100
            #如果曲线运动到边界了，就需要隐藏。
            if x+130>370:
                continue
            #把点放到polygon，方便画折线
            polygon.append(QPoint(x+130, y))
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        # 设置QPainter.Antialiasing, True反走样，否则，你会看到咱们画出的线是锯齿状的……
        painter.setRenderHint(QPainter.Antialiasing, True)
        #两点确定一条直线  画坐标轴
        painter.drawLine(130,160,370,160)#x轴
        painter.drawLine(130,160,130,70)#y轴
        #画y轴的各种数值
        # for i in range(0,100,10):
        #     painter.drawText(105,160-i,str(i))
        for i, value in enumerate(np.linspace(0, 1, 11)):
            painter.drawText(105, 160 - i * 10, str(round(value, 1)))

        #x轴下标
        painter.drawText(360,175,'t')
        #测试点painter.drawText(360,70,'.')
        #画一个图的四面边框
        pen.setColor(Qt.black)
        painter.setPen(pen)
        #四条边
        painter.drawLine(100,190,100,40)
        painter.drawLine(100,190,400,190)
        painter.drawLine(100,40,400,40)
        painter.drawLine(400,190,400,40)
        painter.drawText(240,210,"结果")
        # 画折线
        pen.setColor(Qt.darkCyan)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setOpacity(1)
        painter.drawPolyline(polygon)  # 传入点集

        #第二个图
        #四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 40, 900, 40)
        painter.drawLine(600, 40, 600, 190)
        painter.drawLine(600, 190, 900, 190)
        painter.drawLine(900, 190, 900, 40)
        painter.drawText(740, 210, "偏转角")
        #x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,160,630,70)
        painter.drawLine(630,160,870,160)
        # x轴下标
        painter.drawText(860, 175, 't')
        #y轴各种数值
        for i in range(0,10,10):
            painter.drawText(605,130-i,str(i))
        #三条折线的点集
        polygon1 = QPolygon()
        for i,data in enumerate(self.datas1):
            x = i * self.pointDistance
            y=160-data*20
            #如果曲线运动到边界了，就需要隐藏。
            if x+630>870:
                continue
            #把点放到polygon，方便画折线
            polygon1.append(QPoint(x+630, y))
        painter.drawPolyline(polygon1)

        polygon2 = QPolygon()
        for i,data in enumerate(self.datas2):
            x = i * self.pointDistance
            y=160-data*20
            #如果曲线运动到边界了，就需要隐藏。
            if x+630>870:
                continue
            #把点放到polygon，方便画折线
            polygon2.append(QPoint(x+630, y))
        painter.drawPolyline(polygon2)

        polygon3 = QPolygon()
        for i,data in enumerate(self.datas3):
            x = i * self.pointDistance
            y=160-data*20
            #如果曲线运动到边界了，就需要隐藏。
            if x+630>870:
                continue
            #把点放到polygon，方便画折线
            polygon3.append(QPoint(x+630, y))
        painter.drawPolyline(polygon3)


        #第三个图
        #四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(100, 230, 400, 230)
        painter.drawLine(100, 230, 100, 380)
        painter.drawLine(100, 380, 400, 380)
        painter.drawLine(400, 380, 400, 230)
        painter.drawText(240, 400, "加速度X")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,350,130,260)
        painter.drawLine(130,350,370,350)

        ''''''
        painter.drawText(360, 365, 't')
        polygon4 = QPolygon()
        for i, data in enumerate(self.datas_x):
            x = i * self.pointDistance
            y = 300 - data*50  #应该是350 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 130 > 370:
                continue
            # 把点放到polygon，方便画折线
            polygon4.append(QPoint(x + 130, y))
        painter.drawPolyline(polygon4)

        ''''''

        # 第四个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 230, 900, 230)
        painter.drawLine(600, 230, 600, 380)
        painter.drawLine(600, 380, 900, 380)
        painter.drawLine(900, 380, 900, 230)
        painter.drawText(740, 400, "加速度Y")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,350,630,260)
        painter.drawLine(630,350,870,350)

        ''''''
        painter.drawText(860, 365, 't')
        polygon5 = QPolygon()
        for i, data in enumerate(self.datas_y):
            x = i * self.pointDistance
            y = 300 - data*50  # 应该是350 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 630 > 870:
                continue
            # 把点放到polygon，方便画折线
            polygon5.append(QPoint(x + 630, y))
        painter.drawPolyline(polygon5)

        ''''''

        # 第五个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(100, 420, 400, 420)
        painter.drawLine(100, 420, 100, 570)
        painter.drawLine(100, 570, 400, 570)
        painter.drawLine(400, 570, 400, 420)
        painter.drawText(240, 590, "加速度Z")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,540,130,450)
        painter.drawLine(130,540,370,540)

        ''''''
        painter.drawText(360, 555, 't')
        polygon6 = QPolygon()
        for i, data in enumerate(self.datas_z):
            x = i * self.pointDistance
            y = 500 - data*20  # 应该是540 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 130 > 370:
                continue
            # 把点放到polygon，方便画折线
            polygon6.append(QPoint(x + 130, y))
        painter.drawPolyline(polygon6)

        ''''''

        # 第六个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 420, 900, 420)
        painter.drawLine(600, 420, 600, 570)
        painter.drawLine(600, 570, 900, 570)
        painter.drawLine(900, 570, 900, 420)
        painter.drawText(740, 590, "风压")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,540,630,450)
        painter.drawLine(630,540,870,540)

        ''''''
        painter.drawText(860, 555, 't')
        polygon7 = QPolygon()
        for i, data in enumerate(self.datas_fengya):
            x = i * self.pointDistance
            y = 540 - data/10  # 应该是540 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 630 > 870:
                continue
            # 把点放到polygon，方便画折线
            polygon7.append(QPoint(x + 630, y))
        painter.drawPolyline(polygon7)

        ''''''

        # 第七个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(100, 610, 400, 610)
        painter.drawLine(100, 610, 100, 760)
        painter.drawLine(100, 760, 400, 760)
        painter.drawLine(400, 760, 400, 610)
        painter.drawText(240, 780, "电阻")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,730,130,640)
        painter.drawLine(130,730,370,730)

        ''''''
        painter.drawText(360, 745, 't')
        polygon9 = QPolygon()
        for i, data in enumerate(self.datas_dianzu):
            x = i * self.pointDistance
            y = 730 - data/100  # 应该是730 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 130 > 370:
                continue
            # 把点放到polygon，方便画折线
            polygon9.append(QPoint(x + 130, y))
        painter.drawPolyline(polygon9)

        ''''''

        # 第八个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 610, 900, 610)
        painter.drawLine(600, 610, 600, 760)
        painter.drawLine(600, 760, 900, 760)
        painter.drawLine(900, 760, 900, 610)
        painter.drawText(740, 780, "温度")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,730,630,640)
        painter.drawLine(630,730,870,730)

        ''''''
        painter.drawText(860, 745, 't')
        polygon_10 = QPolygon()
        for i, data in enumerate(self.datas_wendu):
            x = i * self.pointDistance
            y = 730 - data # 应该是540 - data 因为是负数，不显示，所以要修改一下坐标
            # 如果曲线运动到边界了，就需要隐藏。
            if x + 630 > 870:
                continue
            # 把点放到polygon，方便画折线
            polygon_10.append(QPoint(x + 630, y))
        painter.drawPolyline(polygon_10)

        ''''''


class CPUstatus(QWidget):
    def __init__(self):
        producer.start()
        consumer.start()

        super(CPUstatus, self).__init__()
        self.resize(1000,800)#宽1000，高800
        self.factory = Demo(self,consumer)
        self.factory.resize(1000, 800)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    platform = CPUstatus()
    platform.show()
    sys.exit(app.exec_())
