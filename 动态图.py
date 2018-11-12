from PyQt5.QtCore import QPoint, QRect, QTimer, Qt
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np
#下面这个类用来模拟获取数据
class Data:
    def __init__(self):
        self.data=np.random.randint(0,20)#随机生成一个0到20的数
    def GetData(self):
        return self.data


class Demo(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self, parent)
        self.timer=QTimer()
        #触发器
        self.timer.timeout.connect(self.TimeAction)
        self.datas=[]
        self.datas1=[]
        self.datas2=[]
        self.datas3=[]
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
        #在这个地方应该设置一个从容器中读取数据的代码，我用简陋的代码模拟一下
        data=Data().data
        #头插法不断插入到总datas里
        self.datas.insert(0,data)
        self.datas1.insert(0,Data().data)
        self.datas2.insert(0,Data().data+20)
        self.datas3.insert(0,Data().data+40)
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
            y=160-data
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
        for i in range(0,100,10):
            painter.drawText(105,160-i,str(i))
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
        painter.drawText(240,210,"图1")
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
        painter.drawText(740, 210, "图2")
        #x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,160,630,70)
        painter.drawLine(630,160,870,160)
        # x轴下标
        painter.drawText(860, 175, 't')
        #y轴各种数值
        for i in range(0,100,10):
            painter.drawText(605,160-i,str(i))
        #三条折线的点集
        polygon1 = QPolygon()
        for i,data in enumerate(self.datas1):
            x = i * self.pointDistance
            y=160-data
            #如果曲线运动到边界了，就需要隐藏。
            if x+630>870:
                continue
            #把点放到polygon，方便画折线
            polygon1.append(QPoint(x+630, y))
        painter.drawPolyline(polygon1)

        polygon2 = QPolygon()
        for i,data in enumerate(self.datas2):
            x = i * self.pointDistance
            y=160-data
            #如果曲线运动到边界了，就需要隐藏。
            if x+630>870:
                continue
            #把点放到polygon，方便画折线
            polygon2.append(QPoint(x+630, y))
        painter.drawPolyline(polygon2)

        polygon3 = QPolygon()
        for i,data in enumerate(self.datas3):
            x = i * self.pointDistance
            y=160-data
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
        painter.drawText(240, 400, "图3")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,350,130,260)
        painter.drawLine(130,350,370,350)

        # 第四个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 230, 900, 230)
        painter.drawLine(600, 230, 600, 380)
        painter.drawLine(600, 380, 900, 380)
        painter.drawLine(900, 380, 900, 230)
        painter.drawText(740, 400, "图4")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,350,630,260)
        painter.drawLine(630,350,870,350)
        # 第五个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(100, 420, 400, 420)
        painter.drawLine(100, 420, 100, 570)
        painter.drawLine(100, 570, 400, 570)
        painter.drawLine(400, 570, 400, 420)
        painter.drawText(240, 590, "图5")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,540,130,450)
        painter.drawLine(130,540,370,540)
        # 第六个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 420, 900, 420)
        painter.drawLine(600, 420, 600, 570)
        painter.drawLine(600, 570, 900, 570)
        painter.drawLine(900, 570, 900, 420)
        painter.drawText(740, 590, "图6")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,540,630,450)
        painter.drawLine(630,540,870,540)
        # 第七个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(100, 610, 400, 610)
        painter.drawLine(100, 610, 100, 760)
        painter.drawLine(100, 760, 400, 760)
        painter.drawLine(400, 760, 400, 610)
        painter.drawText(240, 780, "图7")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(130,730,130,640)
        painter.drawLine(130,730,370,730)
        # 第八个图
        # 四条边
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(600, 610, 900, 610)
        painter.drawLine(600, 610, 600, 760)
        painter.drawLine(600, 760, 900, 760)
        painter.drawLine(900, 760, 900, 610)
        painter.drawText(740, 780, "图8")
        # x,y坐标
        pen.setColor(Qt.darkCyan)
        painter.setPen(pen)
        painter.drawLine(630,730,630,640)
        painter.drawLine(630,730,870,730)


class CPUstatus(QWidget):
    def __init__(self):
        super(CPUstatus, self).__init__()
        self.resize(1000,800)#宽1000，高800
        self.factory = Demo(self)
        self.factory.resize(1000, 800)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    platform = CPUstatus()
    platform.show()
    sys.exit(app.exec_())
