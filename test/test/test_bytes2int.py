#@Time    :2018/10/29 19:46
import tool.bytes2int as bi

#在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的
#https://www.cnblogs.com/R-bear/p/7744454.html
b = b'abcd'
res = bi.bytes2Int32(b)
print(res)

res = bi.bytes2Int16(b)
print(res)

res = bi.bytes2UInt16(b)
print(res)
