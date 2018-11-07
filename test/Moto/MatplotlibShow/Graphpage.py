from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GraphPage(QWidget):
    def __init__(self):
        super(GraphPage,self).__init__()

        #set figure
        self.figure = plt.figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.show()
        self.toolsbar = NavigationToolbar2QT(self.canvas, self)
        self.toolsbar.update()

        #set axes
        self.ax = self.figure.add_subplot(111)

        #set layout
        self.graphLayout = QtWidgets.QVBoxLayout(self)
        self.graphLayout.addWidget(self.canvas)
        self.graphLayout.addWidget(self.toolsbar)

    #animate function
    def animate(self,i):
        pullData = open(Filepath, "r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(float(y))
        self.ax.clear()
        self.ax.plot(xList, yList, label='a')
        self.ax.plot(xList, [10] * len(yList), label='b')
        self.ax.plot(xList, [11] * len(yList), label='c')

def Mainloop(filepath):
    global Filepath
    Filepath = filepath
    app = QApplication([])
    page = GraphPage()
    ani = animation.FuncAnimation(page.figure, page.animate, interval=100)
    page.show()
    app.exit(app.exec_())

if __name__ == '__main__':
    Mainloop("sampleText.txt")