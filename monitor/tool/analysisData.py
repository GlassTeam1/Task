#@Time    :2018/10/30 10:55

import tool.const as const
from tool.data_type import *

'''
定义常量
'''
const.ACCELEROMETERTYPE = 2; #加速计类型
const.ELECTRICRESISTANCESTRAINTYPE = 32;# 电阻应变类型
const.TEMPERATURETYPE = 1; #温度类型

'''
接收到数据str之后对其进行解析
'''
def analysisData(primaryData):
    if primaryData[0] != 173:
        return
    data = SerialData(primaryData)
    type = b2i.bytes2Int16(data.sensorType) #获取上传数据的设备类型

    '''
    根据传感器类型创建对应的对象、并做对应的处理
    '''
    if type == const.ACCELEROMETERTYPE:
        device = Accelerometer()
    elif type == const.ELECTRICRESISTANCESTRAINTYPE:
        device = ElectricResistanceStrain()
    elif type == const.TEMPERATURETYPE:
        device = Temperature()
    else:
        print("2-------当前测试数据不满足规范-------")
        return
    device.parseData(primaryData)  #执行数据解析

    '''
    调用启动数据存储模块
    '''
    print("1--------------------------")
    print(device.attributes)
    print(device.telemetry)