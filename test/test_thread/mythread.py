#@Time    :2018/11/9 17:35
import threading
import time
class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print('Thread Object(%d),Time:%s\n'%(self.thread_num,time.ctime()))
            time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True

def test():
    thread1 = timer(1,1)
    thread2 = timer(2,2)
    thread3 = timer(3,3)

    thread1.start()
    thread2.start()
    thread3.start()

    time.sleep(6)
    thread1.stop()
    thread2.stop()
    thread3.stop()

if __name__ == '__main__':
    test()