#@Time    :2018/10/29 19:36
from numpy import *

#byte类型的数组转成32位的数字
def bytes2Int32(bytes):
    int32_ = int32(0);
    for i in range(4):
        int32_ = int32_ << 8
        int32_ = int32_ | (bytes[i] & 0xFF)
    return  int32(int32_)

#byte类型的数组转成16位的数字
def bytes2Int16(bytes):
    int16_ = int16(0);
    for i in range(2):
        int16_ = int16_ << 8
        int16_ = int16_ | (bytes[i] & 0xFF)
    return int16(int16_)


#byte类型的数组转成16位的数字(无符号)
def bytes2UInt16(bytes):
    uint16_ = uint16(0);
    for i in range(2):
        uint16_ = uint16_ << 8
        uint16_ = uint16_ | (bytes[i] & 0xFF)
    return uint16(uint16_)

