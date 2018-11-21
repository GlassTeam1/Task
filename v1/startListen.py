#@Time    :2018/10/30 10:21
import serial.tools.list_ports
import const as const
import bytes2int as b2i

'''
定义常量
'''
const.BAUDRATE = 38400 #波特率
const.DATABITS = 8 #数据位
const.STOPBITS = 1 #终止位
class StartListen:
    def __init__(self):
        print("初始化串口监听。。。。。")
        self.serialPort = self.configSerial()
        print("串口监听初始化完成！！！")

    '''
    
    '''
    def getPrimaryData(self):
        '''
        每次取4组（取其中三组为有效数据），每组长度13
        改进 每次开始的位置修改为包含数据类型的  每次都从1开始，然后是2，接下来是32，，
        因为传感器传过来的数据是按照顺序传输的
        所以每次取的数据的长度是6倍的一组数据的长度
        6 * 13 = 78
        '''
        primaryData = self.serialPort.read(78)
        '''
        截取到有效位
        '''
        index = 0;
        # 如果数据已经查找一半了还没有找到起始位置，则剩下的数据肯定不能满足是完整的一组数据了
        for i in range(int(len(primaryData) / 2) + 1):
            type = b2i.bytes2Int16(primaryData[i + 4:i + 6])
            if (primaryData[i] == 173) and (
                    primaryData[i + 1] == 173) and (
                    type == const.ACCELEROMETERTYPE):
                index = i
                break
        '''
        截取有效长度，并将初始二进制数据返回
        '''
        primaryData = primaryData[index:index + 39]
        # print(primaryData)  # 打印数据
        # print(len(primaryData)) #测试是否能够满足每组截取出来的数据都能获取完整
        return primaryData

    '''
    配置串口连接
    具体的参数配置可以等到前端页面发送过来再进行配置
    '''
    def configSerial(self):
        # 查询打开端口的数量
        #plist = list(serial.tools.list_ports.comports())
        plist=[]
        if len(plist) <= 0:
            print("没有发现端口!")
            # 测试列表
            serialPortName = ['传感器1','传感器2','test']
            return serialPortName
        # else:
        #     # 查询出想要使用的端口（因为只有一个，所以调用第1个）
        #     plist_0 = list(plist[0])
        #     serialName = plist_0[0]
        #     # 获取端口使用权（如果有其他应用也在监听该端口会报端口不可用的错误） serial.Serial（）只能调用一次
        #     '''
        #     配置串口参数  波特率、数据位、终止位
        #     '''
        #     serialPort = serial.Serial(serialName)
        #     serialPort.baudrate = const.BAUDRATE
        #     serialPort.bytesize = const.DATABITS
        #     serialPort.stopbits = const.STOPBITS
        #
        #     print("可用端口名>>>", serialPort.name)
        #     return serialPort

# if __name__=='__main__':
#     print(StartListen().serialPort)