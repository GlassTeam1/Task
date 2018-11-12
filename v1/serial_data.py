#@Time    :2018/10/29 21:31

'''
初步解析从串口监听到的数据
'''
class SerialData:
    def __init__(self,primaryData):
        #Python slice() 函数用法
        self.header = primaryData[0:2]
        self.mcuId = primaryData[2:4]
        self.sensorType = primaryData[4:6]
        self.payLoad = primaryData[6:12]
        self.chk = primaryData[12:13]
