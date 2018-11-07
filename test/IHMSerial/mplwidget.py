"""Matplotlib QtDesigner Widget."""


from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MplCanvas(FigureCanvasQTAgg):
    """MplCanvas."""

    def __init__(self):
        """Init."""
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, self.fig)
        FigureCanvasQTAgg.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

    def plot(self, x, y, title=""):
        """Plot deformée."""
        self.ax1.cla()
        self.ax1.set_title(title)
        self.ax1.plot(x, y)
        self.draw()


class MplWidget(QtWidgets.QWidget):
    """QtDesigner QtWidget Promotion Class."""

    def __init__(self, parent=None):
        """Init."""
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def set_figure(self):
        """Set figure."""
        self.canvas.subplots()
