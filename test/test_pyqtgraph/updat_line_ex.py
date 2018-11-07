#@Time    :2018/11/3 14:41

"""
Update a simple plot as rapidly as possible to measure speed.
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time

app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
p.setRange(QtCore.QRectF(0, -10, 5000, 20))
p.setLabel('bottom', 'Index', units='B')
curve = p.plot()

# curve.setFillBrush((0, 0, 100, 100))
# curve.setFillLevel(0)

# lr = pg.LinearRegionItem([100, 4900])
# p.addItem(lr)

data = np.random.normal(size=(50, 5000))
ptr = 0
lastTime = time()
fps = None


def update():
    global curve, data, ptr, p, lastTime, fps
    curve.setData(data[ptr % 10])
    ptr += 1
    now = time()
    dt = now - lastTime
    lastTime = now
    if fps is None:
        fps = 1.0 / dt
    else:
        s = np.clip(dt * 3., 0, 1)
        fps = fps * (1 - s) + (1.0 / dt) * s
    p.setTitle('%0.2f fps' % fps)
    app.processEvents()  ## 强制完成每个绘图的重绘。


timer = QtCore.QTimer()
timer.setInterval(1)
timer.start()
timer.timeout.connect(update)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
