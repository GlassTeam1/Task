#@Time    :2018/10/30 10:55
import random
import time
import const as const
from data_type import *


'''
定义常量
'''
const.ACCELEROMETERTYPE = 2; #加速计类型
const.ELECTRICRESISTANCESTRAINTYPE = 32;# 电阻应变类型
const.TEMPERATURETYPE = 1; #温度类型
count = 0;

class AnalysisData:

    def __init__(self):
        self.engine = self.MatlabEngine()

        print("数据解析模块初始化成功！！！")

    def MatlabEngine(self):
        print("Matlab引擎加载中。。。")
        time.sleep(5)
        print("Matlab引擎加载成功！！！")
        return 1
    '''
    接收到数据str之后对其进行解析
    调用Matlab算法计算结果
    '''
    def dealWithData(self,primaryData):
        '''
        直接将传递过来的完整的一组数据按照规范进行拆分
        每组接受到的数据的顺序都是按照类型2   32   1 这样的顺序发送过来的
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
        在返回结果处加入模拟数据
        将产生的随机数添加到返回结果中，这些随机数的所属类型分别为：压力;拉力;偏转角1--9的x,y,z;四阶频率；结果
        '''
        #风压的数值范围100~400，幅度为20，产生方式为：100为基数，在100上面加上随机个20，上限为400 即随机数的范围是（400-100）/20 = 1~15
        Load_C = 100+20*random.randint(1,15) #生成1到15之间的随机整数
        #Load_T = 100+20*random.random(1,15)  #在界面上只需要显示一个即可

        #转角数据范围是0.1~5，变化幅度为0.5，产生方式为：0.1为基数，在0.1上面加上随机个0.5，上限为5 即随机数的范围是（5-0.1）/0.5 = 1~9
        #因为在界面上显示的是一个转角的数据，暂时只需要复制3份即可
        URX1_C = 0.1+0.5*random.randint(1,9) #将这个数值复制 6*9 = 54 次，暂时只用到3份即可
        URY1_C = 0.1 + 0.5 * random.randint(1, 9)
        URZ1_C = 0.1 + 0.5 * random.randint(1, 9)

        #第一、二、三、四阶自振频率的计算方式是通过加速度的值计算出来的，即使用数据device_1.telemetry.x；device_1.telemetry.y；device_1.telemetry.z
        #暂时没有计算公式，可采用模拟数据的方式（暂时不使用该项数据）
        # Frequency_1 = random.random()
        # Frequency_2 = random.random()
        # Frequency_3 = random.random()
        # Frequency_4 = random.random()

        #因为在演示的过程中调用MATLAB程序需要在本地电脑安装MATLAB（还没有找到打包MATLAB程序的方式，需要研究算法的一方提供打包好的文件），因此结果也采用模拟方式
        #结果数据解释说明：结果数据的范围是0~1，0.3~0.5 玻璃处于较危险状态；0.5~1 玻璃处于严重危险状态；0~0.3 玻璃处于安全状态（暂定模拟数据的范围在这个范围内）
        result = random.random()  # 产生0~1的随机浮点数


        return [device_1.telemetry.x,device_1.telemetry.y,device_1.telemetry.z,device_2.telemetry.strain,device_3.telemetry.temperature,
                Load_C,URX1_C,URY1_C,URZ1_C,result]