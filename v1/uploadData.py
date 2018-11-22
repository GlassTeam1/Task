#@Time    :2018/10/30 10:19
'''
上传数据到数据库
'''
import pymysql
import datetime

'''
配置数据库连接
'''

class InterfaceDatabaseOperation(object):#数据库操作虚拟接口
    def link(self):pass
    def search(self): pass
    def add(self):pass

class ImplLink(InterfaceDatabaseOperation):#数据库连接
    def __init__(self):
        pass
    def link(self):
        db = pymysql.connect(host='rm-uf61rus51t9u8eb79no.mysql.rds.aliyuncs.com',  # 远程主机的ip地址，
                                     user='root',  # MySQL用户名
                                     db='xian',  # database名
                                     passwd='root@123',  # 数据库密码
                                     port=3306,  # 数据库监听端口，默认3306
                                     charset="utf8")  # 指定utf8编码的连接
        print("数据库连接成功！")
        return db

class ImplAdd(InterfaceDatabaseOperation):#添加数据
    def __init__(self,db):
        self.db = db

    def add(self, data):
        print(data)
        now_time = datetime.datetime.now()
        count=0
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # 插入操作
        sql = "INSERT INTO `xian`.`testdata` (`datas_x`,`datas_y`,`datas_z`,`datas_dianzu`,`datas_wendu`,`datas_fengya`,\
                    `datas1`,`datas2`,`datas3`,`datas`,`time`) VALUES ('%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%s') ;"
        try:
            #self.db.ping(reconnect=True)
            cursor.execute(sql % (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],now_time.strftime('%Y-%m-%d %H:%M:%S')))
            self.db.commit()
        except:
            self.db.rollback()

class ImplSearch(InterfaceDatabaseOperation):#数据库搜索
    def __init__(self,queue,db):
        self.dataname=queue#传入dataname数组
        self.db = db

    def Isearch(self,tablename):#sql语句执行搜索最后一条

        cursor = self.db.cursor()
        sql="select * from  %s  order by idtestdata desc limit 1 "
        try:
            #print(sql%(tablename))
            cursor.execute(sql%(tablename))
            result = cursor.fetchone()
           # print(result[0])
            return result
        except:
            self.db.rollback()


    def search(self):#对dataname中每一个名字进行sql搜索，results存储最后一条结果
        results = []
        for i in self.dataname:
            #print(i)
            result = self.Isearch(i)
            results.append(result)
        return results

