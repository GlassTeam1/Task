#@Time    :2018/10/30 10:21
import serial.tools.list_ports
import tool.const as const
import tool.analysisData as ad
'''
定义常量
'''
const.BAUDRATE = 38400 #波特率
const.DATABITS = 8 #数据位
const.STOPBITS = 1 #终止位

'''
打开串口监听数据
'''
# 查询打开端口的数量
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    # 查询出想要使用的端口（因为只有一个，所以调用第1个）
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    # 获取端口使用权（如果有其他应用也在监听该端口会报端口不可用的错误）
    # serial.Serial（）只能调用一次
    '''
    配置串口参数  波特率、数据位、终止位
    '''
    serialPort = serial.Serial(serialName)
    serialPort.baudrate = const.BAUDRATE
    serialPort.bytesize = const.DATABITS
    serialPort.stopbits = const.STOPBITS

    print("可用端口名>>>", serialPort.name)

    '''
    实时监听数据，定时取点分割
    '''
    # 测试发送及接收数据
    # encode():使用该函数将要发送的数据转化为二进制数据
    n = serialPort.write(b'you are my world\r\naaaaaaaaaaaaa\r\nbbbbbbbbbbbbb\r\n')  # n获取发送数据的长度

    print(n)  # 打印数据长度

    '''
    通过比较数据长度是否符合协议要求舍弃脏数据
    '''
    while True:
        primaryData = serialPort.readline()
        print(primaryData)
        length = len(primaryData)

        #比协议规定的13位多出来两位  即'\r\n'的位置
        if length== 15:
            '''
            调用启动数据解析模块
            '''
            print(primaryData)  # 打印数据
            ad.analysisData(primaryData)