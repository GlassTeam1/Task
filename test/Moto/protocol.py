'''
value_0x=0x0706050403020100
进入的数字一共8个字节，对应B7,B6,B5,B4,B3,B2,B1,B0，本函数提出所有低四位。
输入格式：
B7：低四位为F1：要数据。为F2：设置参数。为F3：开始。为F4：停止。
B6：电机型号，01 A，02 B，03 C，04 D。
B5：需要设置的参数，当B7不为02输出NONE。
B4-B0：数字，B0是6-4bit移位。
B0的最高位bit7是符号位
B0最后4bits（0-3bit）作为校验
回复四个参数，第一个是B7代表的字符串；第二个参数：返回几号电机；第三个参数：设置参数01-80；第四个参数：把一个数值发出来
'''
import binascii
import re

def convert(value_str):
    value_str = value_str[2:len(value_str)]
    value_0x = binascii.a2b_hex(value_str)
    if(len(value_str)!=16):
        print('需要8bytes')
        return False
    #提取B0到B7位
    B0 = value_0x[7]
    B1 = value_0x[6]
    B2 = value_0x[5]
    B3 = value_0x[4]
    B4 = value_0x[3]
    B5 = value_0x[2]
    B6 = value_0x[1]
    B7 = value_0x[0]
    B0_mark = B0 & 0x80
    B0_mark = B0_mark >> 7
    B0_jud = B0 & 0x0F
    B0 = B0&0x70
    B0 = B0 >> 4
    B4_B1 = B1 + B2 * 256 + B3 * 256 * 256 + B4 * 256 * 256 * 256
    if((B7 & 0xF0)!=0xF0):
        print('协议头出问题了，需要前4位1111')
        return False
    B7=B7&0x0F
    if(B0_jud!=0xF):
        print('协议尾出问题了，需要后4位1111')
        return False

    #电机处理
    if B6 == 0x01:
        value_B6 = ["Motor_A"]
    elif B6 == 0x02:
        value_B6 = ["Motor_B"]
    elif B6 == 0x03:
        value_B6 = ["Motor_C"]
    elif B6 == 0x04:
        value_B6 = ["Motor_D"]
    else:
        print('电机参数错误')
        return False

    #类型处理阶段
    if B7 == 0x01:
        value_B7 = ["in"]
        if B5 < 81:
            value_B5 = [B5]
        else:
            print('设置参数超过80范围')
            return False
        return value_B7 + value_B6 + value_B5

    elif B7 == 0x02:
        value_B7 = ["out"]
        #处理参数3
        if B5 < 81:
            value_B5 = [B5]
            #处理参数4
            if (B0_mark):
                value_B4_B1 = [-(B4_B1 / (10 ** B0))]
            else:
                value_B4_B1 = [B4_B1 / (10 ** B0)]
        else:
            print('设置参数超过80范围')
            return False
        return value_B7 + value_B6 + value_B5 + value_B4_B1

    elif B7 == 0x03:
        value_B7 = ["begin"]
        return value_B7 + value_B6

    elif B7 == 0x04:
        value_B7 = ["stop"]
        return value_B7 + value_B6

    elif B7 == 0x07:
        value_B7 = ["warning"]
        # 处理参数3
        if B5 < 13:
            value_B5 = [B5]
        else:
            print('设置参数超过12范围')
            return False
        return value_B7 + value_B6 + value_B5
    elif B7 == 0x08:
        value_B7 = ["time"]
        value_B4_B1 = [B4_B1]
        return value_B7 + value_B6 + value_B4_B1
    else:
        print("B7超越范围")
        return False

def de_convert(Info):
    #开始发数据和关闭发数据
    if type(Info) is str:
        if(Info == 'start'):
            return hex(0xf50000000000000f)
        elif(Info == 'stop'):
            return hex(0xf60000000000000f)
        else:
            print('错误str')
            return False
    #判断电机
    if Info[1] == "Motor_A":
        B6 = 0x01
    elif Info[1] == "Motor_B":
        B6 = 0x02
    elif Info[1] == "Motor_C":
        B6 = 0x03
    elif Info[1] == "Motor_D":
        B6 = 0x04
    else:
        print('第二个参数电机参数错误')
        return False

    #判断模式
    if Info[0] == "in":
        if len(Info)!=3:
            print('传入信息错误，in模式3个参数')
            return False
        B7 = 0xF1
        #判断参数3
        if not isinstance(Info[2],int):
            print('参数3输入int型变量')
            return False
        if Info[2]>0 and Info[2]<81:
            B5 = Info[2]
            return hex(B7 << 56 | B6 << 48 | B5 << 40 | 0xF)
        else:
            print('参数3范围错误（需要在0-80）')
            return False

    elif Info[0] == "out":
        if len(Info)!=4:
            print('传入信息错误,out模式4个参数')
            return False
        B7 = 0xF2
        #参数3
        if not isinstance(Info[2],int):
            print('参数3输入int型变量')
            return False
        if Info[2]>0 and Info[2]<81:
            B5 = Info[2]
            # 判断参数4
            B4_B1 = float(Info[3])
            if B4_B1 < 0:
                B0_mark = 1 << 7
                B4_B1 = -B4_B1
            else:
                B0_mark = 0
            tmp = str(B4_B1).split('.')[1]
            if(tmp != '0'):
                B0_jud = len(tmp)
            else:
                B0_jud = 0
            B4_B1 = 10**B0_jud*B4_B1
            B4_B0 = (int(B4_B1) << 8) | (B0_jud<<4 )| B0_mark|0xF

            return hex(B7 << 56 | B6 << 48 | B5 << 40 | B4_B0)

        else:
            print('参数3范围错误（需要在1-80）')
            return False

    elif Info[0] == "begin":
        if len(Info)!=2:
            print('传入信息错误,begin模式2个参数')
            return False
        B7 = 0xF3
        return hex(B7 << 56 | B6 << 48 | 0xF )

    elif Info[0] == "stop":
        if len(Info)!=2:
            print('传入信息错误,stop模式2个参数')
            return False
        B7 = 0xF4
        return hex(B7 << 56 | B6 << 48 | 0xF)

    elif Info[0] == 'warning':
        B7 = 0xF7
        # 判断参数3
        if not isinstance(Info[2], int):
            print('参数3输入int型变量')
            return False
        if Info[2] > 0 and Info[2] < 13:
            B5 = Info[2]
            return hex(B7 << 56 | B6 << 48 | B5 << 40 | 0xF)
        else:
            print('参数3范围错误（需要在1-8）')
            return False

    elif Info[0] == 'time':
        B7 = 0xF8
        if(isinstance(Info[2],int)):
            B4_B1 = Info[2]
            return hex(B7 << 56 | B6 << 48 | B4_B1 << 8 | 0xF)
        else:
            print('参数3为整数')
            return False
        #时间判断

    else:
        print('第一个参数错误')
        return False

def judgeRev(hexString):
    ret = []
    while(True):
        #找信息
        tmp_16 = re.search(r'[f][1-47][0][1-4][0-9a-f]'
                  + r'[0-9a-f][0-9a-f][0-9a-f][0-9a-f]'
                  + r'[0-9a-f][0-9a-f][0-9a-f][0-9a-f]'
                  + r'[0-9a-f][0-9a-f][f]', hexString)
        if tmp_16:
            ret += ['0x'+tmp_16.group()]
            hexString = re.sub(tmp_16.group(),'',hexString,count=1)
        '''
        #找回复
        tmp_4 = re.search(r'[f][24][0][f]', hexString)
        if tmp_4:
            ret += ['0x'+tmp_4.group()]
            hexString = re.sub(tmp_4.group(), '', hexString,count=1)
        if (not tmp_4) and (not tmp_16):
            break
        '''
        if not tmp_16:
            break

    if ret == []:
        return False
    else:
        return ret

'''测试用例'''
if __name__ == '__main__':
    b= de_convert(['warning','Motor_A',8])
    b =de_convert(['time','Motor_A',8])
    if b:
        print(b)
        a = convert('0xf20101000000010f')
        if a:
            print(a)
    f = judgeRev('0xf70108000000010ff20108000000010ff20108000000010ff20ff40f')
    print(f)



