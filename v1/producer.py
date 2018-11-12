#@Time    :2018/11/10 14:38
from queue import Queue
import random
import threading
import time
import analysisData as ad

class Producer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        filename = "bytes_data_2018年11月5日.txt"
        my_open = open(filename,'rb')
        while True:
            bytes = my_open.read(39)
            '''
            解析数据  analysisData  
            封装为指定类型  data_type
            '''
            array = ad.analysisData(bytes)
            self.data.put(array)
            '''
            使用时间间断模拟发送频率
            '''
            #time.sleep(0.05)

class Consumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        while True:
            '''
            不断的去消耗数据，防止数据堆积，保障数据的实时性
            同时控制频率
            '''
            val = self.data.get()
            print(val)
            time.sleep(0.10)

    def getData(self):
        print("当前截取到的数据为: %f"%(self.data.get()[0]))
        return self.data.get()

def main():
    queue = Queue(maxsize=100)
    producer = Producer('Pro.',queue)
    consumer = Consumer('Con.',queue)
    producer.start()
    consumer.start()

    time.sleep(3)
    consumer.getData()

if __name__ == '__main__':
    main()