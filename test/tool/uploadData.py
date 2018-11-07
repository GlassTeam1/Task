#@Time    :2018/10/30 10:19
'''
上传数据到数据库
'''

import csv
def uploadData(x,y,z,strain,temperature):

    with open("H:\PythonCode\\test\\tool\data.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(["bytedata", "x", "y","z","strain","temperature"])
        writer.writerow(x,y,z,strain,temperature)