#@Time    :2018/11/1 19:32
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random
#import time
from PyQt5.QtCore import QTimer

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=15, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self,data):
        x = data[0]
        y = data[1]
        self.axes.plot(x, y)

    def test2(self):
        # 新建一个QTimer对象
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.start()
        # 信号连接到槽
        self.timer.timeout.connect(self.data())

        x,y = self.data()
        ax1 = self.axes
        ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
        ax1.grid(True)
        ax1.axhline(0, color='black', lw=2)
        ax1.draw

    def data(self):
        x, y = np.random.randn(2, 100)
        return x,y

    def test3(self):
        #np.random.seed(19680801)

        dt = 0.01
        t = np.arange(0, 30, dt)
        nse1 = np.random.randn(len(t))  # white noise 1
        nse2 = np.random.randn(len(t))  # white noise 2

        # Two signals with a coherent part at 10Hz and a random part
        s1 = np.sin(2 * np.pi * 10 * t) + nse1
        s2 = np.sin(2 * np.pi * 10 * t) + nse2

        axs = self.axes
        # axs.plot(t, s1, t, s2)
        # axs.set_xlim(0, 2)
        # axs.set_xlabel('time')
        # axs.set_ylabel('s1 and s2')
        # axs.grid(True) #显示线条

        cxy, f = axs.cohere(s1, s2, 256, 1. / dt)
        axs.set_ylabel('coherence')

