#@Time    :2018/11/9 18:00
from queue import Queue
import random
import threading
import time

class Producer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        filename = "H:\\task\\Task\\bytes_data_2018年11月5日.txt"
        my_open = open(filename,'rb')
        i =0
        while True:
            #bytes = my_open.read(39)
            #str = len(bytes)
            i= i+1
            self.data.put(i)
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        while True:
            val = self.data.get()
            #print("当前队列长度：%d"%(self.data.qsize))
            print(val)
            time.sleep(0.01)

def main():
    queue = Queue(maxsize=10)
    producer = Producer('Pro.',queue)
    consumer = Consumer('Con.',queue)
    producer.start()
    consumer.start()

if __name__ == '__main__':
    main()