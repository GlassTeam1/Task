#@Time    :2018/10/29 20:56
from tool.data_type import *
from tool.serial_data import *


a = Accelerometer()
a.parseData(primaryData=b'abcdefghijklmn')
print(a.telemetry.x)
print(a.telemetry.y)
print(a.telemetry.z)
print(a.telemetry)
print(a.attributes)


serialData = SerialData(primaryData=b'abcd')
print(serialData.header)