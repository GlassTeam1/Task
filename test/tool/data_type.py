#@Time    :2018/10/29 19:32
import tool.bytes2int as b2i
from tool.serial_data import *
import numpy as numpy

class Accelerometer_Telemetry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class ElectricResistanceStrain_Telemetry:
    def __init__(self):
        self.strain = 0

class Temperature_Telemetry:
    def __init__(self):
        self.temperature = 0

'''
加速度器的构造函数
其中
telemetry为检测到的数据 x,y,z 为数据的值
attributes为设备属性
parseData()方法为解析数据的方法
'''
class Accelerometer:
    def __init__(self):
        self.telemetry = Accelerometer_Telemetry()
        self.attributes = 0

    def parseData(self,primaryData):
        '''
        再次调用初步解析串口数据的方法
        （这里应该直接指定primaryData就是解析好的对象，暂时没找到解决办法，优化时对其修改）
        '''
        data = SerialData(primaryData)
        self.telemetry.x = b2i.bytes2Int16(data.payLoad[0:2])/16834.0
        self.telemetry.y = b2i.bytes2Int16(data.payLoad[2:4])/16834.0
        self.telemetry.z = b2i.bytes2Int16(data.payLoad[4:6])/16834.0
        self.attributes = b2i.bytes2UInt16(data.mcuId)

'''
电阻应变的构造函数
telemetry 为检测到的数据
attributes为设备属性
parseData()方法为解析数据的方法
'''
class ElectricResistanceStrain:
    def __init__(self):
        self.telemetry = ElectricResistanceStrain_Telemetry()
        self.attributes = 0

    def parseData(self,primaryData):
        data = SerialData(primaryData)
        st = b2i.bytes2Int32(data.payLoad)
        tt = (1 / (2.048 * st / 3.3 / pow(2, 23) + 1) - 1) * pow(10, 6)
        if tt < -50000.0 or tt > 50000.0:
            tt = 0
        self.telemetry.strain = tt
        self.attributes = b2i.bytes2UInt16(data.mcuId)

'''
温度的构造函数
telemetry为检测到的数据
attributes为设备属性
parseData()方法为解析数据的方法
'''
class Temperature:
    def __init__(self):
        self.telemetry =Temperature_Telemetry()
        self.attributes = 0

    def parseData(self,primaryData):
        data = SerialData(primaryData)
        n = b2i.bytes2Int32(data.payLoad)
        k = n / pow(2, 25) * 2.048 / 2.7
        tt = (240 / (1 - 2 * k) - 220) * 50 / 19.4 - 7
        if tt < -20 or tt > 60:
            tt = 0

        self.telemetry.temperature = tt
        self.attributes = b2i.bytes2UInt16(data.mcuId)