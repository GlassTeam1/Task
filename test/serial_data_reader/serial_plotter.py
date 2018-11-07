import csv
import sys
import logging
import time
from datetime import datetime
from pathlib import Path
from threading import Thread

import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox, QHBoxLayout, QDialog, \
    QVBoxLayout, QCheckBox

from serial import Serial

import pyqtgraph as pg

from serial_data_reader.helpers import configure_serial
import serial.tools.list_ports

EXPORT_TO = './exports'
DEFAULT_DT = 0.05


class Communicator(QObject):
    update_ui = pyqtSignal(list)
    update_filtered_curves = pyqtSignal(int, bool)


class SerialReader:
    def __init__(self, communicator: Communicator, ):
        self._communicator = communicator
        self._ser = Serial()
        self._columns = None
        self._dt = None
        self._run = False
        self._serial_task = Thread(target=self.serial_task)

    def start(self, port, baudrate, columns: int, dt: float):
        self._columns = columns
        self._dt = dt
        self._ser.port = port.device
        self._ser.baudrate = baudrate
        self._ser.open()
        self._run = True
        self._serial_task.start()

    def stop(self):
        self._run = False
        if self._serial_task.is_alive():
            self._serial_task.join()

    def serial_task(self):
        """
        流程任务 我们阅读所有内容，我们分成几行，我们将每个分成值。
         累积值并将其发送到接口流。
        """
        while self._run:
            time.sleep(self._dt)  # 不是设置接口事件频率的最佳方法，但它可以工作

            batch_data = []

            #byte_data = self._ser.read_all().split(b'\r\n')
            byte_data = csv.reader(open('H:\PythonCode\\test\serial_data_reader\example.csv','r'))

            print(byte_data)
            for line in byte_data:
                try:
                    print(line)
                    #values = line.split(b';')
                    values = list(map(float, line))  # 转换为浮点数

                    #跳过数据少于预期的行（是的，当读取块时会发生这种情况）
                    #这并不可怕
                    if len(values) == self._columns:
                        batch_data.append(values)

                except ValueError:
                    pass

            if batch_data:
                self._communicator.update_ui.emit(batch_data)  #发送数据


class ViewSettingsWindow(QDialog):
    """
    线可见性编辑窗口
    """
    def __init__(self, communicator, invisible_curves, curves_names, parent=None):
        super().__init__(parent)

        self.communicator = communicator
        self.invisible_curves = invisible_curves
        self.curves_names = curves_names

        # 为每一行创建复选框
        self.buttons_group = []
        for i, (c_name, c_active) in enumerate(zip(self.curves_names, self.invisible_curves)):
            cb = QCheckBox(c_name)
            cb.setChecked(not c_active)  # 复选框在invisible_curves中显示False

            # 我不知道如何在处理程序内传递拳击手的支票号码，只有lambda和闭包，
            # 并且通过kwargs转发lambda内部，否则每个lambda将有最后一个i计数器
            cb.toggled.connect(lambda value, i=i: self.update_checkbox(i, value))
            self.buttons_group.append(cb)

        self.setWindowTitle('View Settings')
        self.setMinimumWidth(150)

        l = QVBoxLayout()
        for b in self.buttons_group:
            l.addWidget(b)

        self.setLayout(l)

    def update_checkbox(self, curve_number, value):
        self.communicator.update_filtered_curves.emit(curve_number, not value)  #标志复选框值被反转


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.communicator = Communicator()

        self.data_pw = pg.PlotWidget(background='#fff')
        self.export_button = QPushButton('Export')
        self.view_settings_button = QPushButton('设置')
        self.clear_button = QPushButton('Clear')
        self.vsw_ViewSettingsWindow = None

        self.serial_reader = SerialReader(self.communicator)

        self.columns = None
        self.data = None
        self.curves = None
        self.curves_names = None
        self.invisible_curves = None

        self.setup_ui()

    def start(self, port, bd, columns, dt):
        self.columns = columns
        self.init_plot(self.columns)
        self.serial_reader.start(port, bd, self.columns, dt)

    def stop(self):
        self.serial_reader.stop()

    def init_plot(self, columns_count):
        """ 按数据中的列数初始化数据矩阵和行对象 """
        self.data_pw.addLegend()
        self.data = [[] for _ in range(columns_count)]
        self.curves_names = [b'column {i+1}' for i in range(columns_count - 1)]
        self.curves = [self.data_pw.plot(pen=pg.intColor(i), name=self.curves_names[i]) for i in range(columns_count - 1)]
        self.invisible_curves = [False for _ in range(columns_count - 1)]  # 显示/隐藏标志

    def setup_ui(self):
        """ 接口初始化 """
        cw = QWidget(self)
        self.setCentralWidget(cw)
        grid_layout = QGridLayout()
        cw.setLayout(grid_layout)

        h_layout = QHBoxLayout()
        top_bar = QWidget(self)
        top_bar.setLayout(h_layout)

        h_layout.addWidget(self.export_button)
        h_layout.addWidget(self.view_settings_button)
        h_layout.addWidget(self.clear_button)
        h_layout.addStretch(1)

        grid_layout.addWidget(top_bar)
        grid_layout.addWidget(self.data_pw)

        self.setMinimumSize(1280, 800)

        # self.data_pw.enableAutoRange()
        self.data_pw.setYRange(0, 100)
        self.data_pw.showGrid(True, True, .5)

        self.export_button.clicked.connect(self.export)
        self.view_settings_button.clicked.connect(self.show_view_settings)
        self.clear_button.clicked.connect(self.clear_data)
        self.communicator.update_ui.connect(self.update_ui)
        self.communicator.update_filtered_curves.connect(self.update_filtered_curves)

    @pyqtSlot()
    def export(self):
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = Path(EXPORT_TO).joinpath(b'export_{date}.csv')
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            data = np.array(self.data).transpose(1, 0)
            writer.writerows(data)

            QMessageBox.about(self, 'Success', b'export file name: "{filename}"')

    @pyqtSlot()
    def show_view_settings(self):
        self.vsw = ViewSettingsWindow(self.communicator, self.invisible_curves, self.curves_names, parent=self)
        self.vsw.show()

    @pyqtSlot()
    def clear_data(self):
        if self.vsw is not None:
            self.vsw.close()

        self.data_pw.clear()
        legend = self.data_pw.plotItem.legend  # 因为土地不属于plotWidget和plotItem
        legend.scene().removeItem(legend)

        self.init_plot(self.columns)

    @pyqtSlot(int, bool)
    def update_filtered_curves(self, curve_number: int, set_invisible: bool):
        """ ViewSettingsWindow中的Slot on change复选框 """
        self.invisible_curves[curve_number] = set_invisible
        if set_invisible:
            self.curves[curve_number].clear()

    @pyqtSlot(list)
    def update_ui(self, batch_values):
        """ 回调，在数据到达时从SerialReader调用 """
        # 更新数据
        for values in batch_values:
            for i, v in enumerate(values):
                self.data[i].append(v)

        # 显示数据
        t, *others = self.data  # 除以时间表和其余部分
        for i, o in enumerate(others):
            if not self.invisible_curves[i]:  # 如果该行未标记为不可见
                self.curves[i].setData(t, o)  # 更新线对象的数据


def configure_self():
    columns_count = 2#int(input('列数: '))
    dt = input('更新周期（秒）（默认为{DEFAULT_DT}）:')
    dt = DEFAULT_DT if dt == '' else float(dt)

    return columns_count, dt


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    port, bd = configure_serial()
    columns, dt = configure_self()

    main_window = MainWindow()
    try:
        main_window.start(port, bd, columns, dt)
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        logging.exception(e)
        sys.exit(1)
    finally:
        main_window.stop()
