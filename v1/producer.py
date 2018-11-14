#@Time    :2018/11/10 14:38
from queue import Queue
import  pymysql
import random
import threading
import time
import v1.analysisData as ad

#threads = []  # 线程元组
class Thread_database():

    def __init__(self):

        self.data=[0,0,0,0,0,0,0,0,0,0]
        self.db=0

    def link(self):
        self.db = pymysql.connect(host='rm-uf61rus51t9u8eb79no.mysql.rds.aliyuncs.com',  # 远程主机的ip地址，
                             user='root',  # MySQL用户名
                             db='xian',  # database名
                             passwd='root@123',  # 数据库密码
                             port=3306,  # 数据库监听端口，默认3306
                             charset="utf8")  # 指定utf8编码的连接

    def update (self,queue):
        self.data=queue
    def run(self):
        count=0
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # 插入操作
        sql = "INSERT INTO `xian`.`testdata` (`datas_x`,`datas_y`,`datas_z`,`datas_dianzu`,`datas_wendu`,`datas_fengya`,\
                    `datas1`,`datas2`,`datas3`,`datas`) VALUES ('%f','%f','%f','%f','%f','%f','%f','%f','%f','%f') ;"

        try:

            #self.db.ping(reconnect=True)

            cursor.execute(sql % (self.data[0],self.data[1],self.data[2], self.data[3],self.data[4],self.data[5], self.data[6], self.data[7], self.data[8], self.data[9]))

            self.db.commit()

        except:

            self.db.rollback()




class Producer(threading.Thread):

    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue
    def run(self):
        filename = "bytes_data_2018年11月5日.txt"
        my_open = open(filename,'rb')
        insert = Thread_database()
        insert.link()
        while True:
        #for i in range (2):
            bytes = my_open.read(39)
            '''
            解析数据  analysisData  
            封装为指定类型  data_type
            '''
            array = ad.analysisData(bytes)
            '''存储array数据到数据库，开启多线程'''
            insert.update(array)
            insert.run()
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