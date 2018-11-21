#@Time    :2018/11/10 14:38
from queue import Queue
import random
import threading
import time

from analysisData import AnalysisData
from startListen import StartListen
from uploadData import Thread_database

'''
生产者：
调用读取串口数据模块
调用串口数据解析模块
将所有数据（包含结果）封装成为元组
'''
class Producer(threading.Thread):

    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

        '''
        将所有需要初始化的部分都放到线程初始化函数中，防止有的模块启动较慢造成数据不一致问题（有可能发生生产者还没生产数据，消费者就去读）
        '''
        # self.listenData = StartListen()
        filename = "bytes_data_2018年11月5日.txt"
        self.listenData = open(filename, 'rb')

        self.analysisData = AnalysisData()
        print("生产者线程初始化成功！！！")

    def run(self):

        while True:
            '''
            读取数据
            '''
            #bytes = self.listenData.getPrimaryData()
            bytes = self.listenData.read(39)

            '''
            解析数据 analysisData
            '''
            array = self.analysisData.dealWithData(bytes)

            '''
            将结果数据push到数据队列
            '''
            self.data.put(array)


'''
消费者：
在run()方法中调用数据库插入模块
getData()方法返回数据，供界面绘图显示调用
'''
class Consumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

        self.insert = Thread_database()
        print("消费者线程初始化成功！！！")

    def run(self):

        while True:
            '''
            调用数据库存储函数
            '''
            val = self.data.get()
            #print(val)
            time.sleep(0.10) #如果存数据操作太快 有可能在getData的时候读不到了吗？
            self.insert.insert(val)

    def getData(self):
        print("当前截取到数据计算得到的结果为: %f"%(self.data.get()[9]))
        return self.data.get()