#@Time    :2018/10/30 10:19
'''
上传数据到数据库
'''
import pymysql

'''
配置数据库连接
'''
class Thread_database():

    def __init__(self):
        self.db = pymysql.connect(host='rm-uf61rus51t9u8eb79no.mysql.rds.aliyuncs.com',  # 远程主机的ip地址，
                             user='root',  # MySQL用户名
                             db='xian',  # database名
                             passwd='root@123',  # 数据库密码
                             port=3306,  # 数据库监听端口，默认3306
                             charset="utf8")  # 指定utf8编码的连接
        print("数据库连接成功！！！")

    '''
    向数据库中插入数据
    '''
    def insert(self,data):
        count=0
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # 插入操作
        sql = "INSERT INTO `xian`.`testdata` (`datas_x`,`datas_y`,`datas_z`,`datas_dianzu`,`datas_wendu`,`datas_fengya`,\
                    `datas1`,`datas2`,`datas3`,`datas`) VALUES ('%f','%f','%f','%f','%f','%f','%f','%f','%f','%f') ;"
        try:
            #self.db.ping(reconnect=True)
            cursor.execute(sql % (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
            self.db.commit()
        except:
            self.db.rollback()