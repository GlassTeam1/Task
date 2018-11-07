#@Time    :2018/11/2 16:30
import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import numpy as np
import time

POINTS = 300
class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")

        # Just some button connected to `plot` method
        self.button = QtWidgets.QPushButton('Plot')
        self.button.clicked.connect(self.plotAnother)

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(20)]
        # create an axis
        ax = self.figure.add_subplot(1,1,1)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data, '*-')
        self.canvas.draw()

    def plotAnother(self):
        for i in range(1000):

            np.random.seed(19680801)
            x, y = np.random.randn(2, 100)
            ax1 = self.figure.add_subplot(1,1,1)
            ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
            ax1.grid(True)
            ax1.axhline(0, color='black', lw=2)
            self.canvas.draw()
            time.sleep(0,10)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())