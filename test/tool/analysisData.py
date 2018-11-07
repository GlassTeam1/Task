#@Time    :2018/10/30 10:55

import tool.const as const
from tool.data_type import *


'''
定义常量
'''
const.ACCELEROMETERTYPE = 2; #加速计类型
const.ELECTRICRESISTANCESTRAINTYPE = 32;# 电阻应变类型
const.TEMPERATURETYPE = 1; #温度类型
count = 0;
'''
接收到数据str之后对其进行解析
'''
def analysisData(primaryData):
    # global count
    # count = count+1
    # if count == 100:
    #     return False
    '''
    直接将传递过来的完整的一组数据按照规范进行拆分
    每组接受到的数据的顺序都是按照类型2   32   1 这样的顺序发送过来的
    :param primaryData:
    :return:
    '''
    #分割数据
    data_1 = primaryData[0:13]
    data_2 = primaryData[13:26]
    data_3 = primaryData[26:39]

    #加载构造器
    device_1 = Accelerometer()
    device_2 = ElectricResistanceStrain()
    device_3 = Temperature()

    #解析数据
    device_1.parseData(data_1)
    device_2.parseData(data_2)
    device_3.parseData(data_3)

    '''
    根据传感器类型创建对应的对象、并做对应的处理
    
    type = b2i.bytes2Int16(data_1.sensorType) #获取上传数据的设备类型
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

    '''
    调用启动数据存储模块
    '''
    #追加的形式
    file_name = "H:\PythonCode\\test\\tool\\bytes_data_2018年11月5日.txt"
    my_open = open(file_name, 'ab')
    # 打开fie_name路径下的文件,采用追加模式
    # 若文件不存在,创建，若存在，追加
    my_open.write(primaryData)
    # my_open.write("x:"+repr(device_1.telemetry.x)+
    #               "y:" + repr(device_1.telemetry.y)+
    #               "z:" + repr(device_1.telemetry.z)+
    #               "strain:" + repr(device_2.telemetry.strain)+
    #               "temperature" + repr(device_3.telemetry.temperature)+'\n')
    my_open.close()

    # with open("H:\PythonCode\\test\\tool\data.csv", "w") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow([device_1.telemetry.x,
    #                     device_1.telemetry.y,
    #                     device_1.telemetry.z,
    #                     device_2.telemetry.strain,
    #                     device_3.telemetry.temperature])
    #print("1---------数据解析完成，正在存储-----------------")
    # print("加速计")
    # #print(device_1.attributes)
    # print("x:"+repr(device_1.telemetry.x))
    # print("y:"+repr(device_1.telemetry.y))
    # print("z:"+repr(device_1.telemetry.z))
    # print("电阻应变")
    # #print(device_2.attributes)
    # print("strain:"+repr(device_2.telemetry.strain))
    # print("温度")
    # #print(device_3.attributes)
    # print("temperature"+repr(device_3.telemetry.temperature))
    return True