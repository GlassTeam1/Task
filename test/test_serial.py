import serial.tools.list_ports

#查询打开端口的数量
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    #查询出想要使用的端口（因为只有一个，所以调用第1个）
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    #获取端口使用权（如果有其他应用也在监听该端口会报端口不可用的错误）
    #serial.Serial（）只能调用一次
    serialFd = serial.Serial(serialName)
    serialFd.baudrate = 38400
    serialFd.bytesize = 8
    serialFd.stopbits = 1

    print("可用端口名>>>", serialFd.name)
    #测试发送及接收数据
    t = serialFd
    #encode():使用该函数将要发送的数据转化为二进制数据
    n = t.write('you are my world'.encode()) #n获取发送数据的长度
    #print (t)
    print (n) #打印数据长度
    str = t.read(n)

    print (str)