import matlab.engine
'''
开始数据分析
'''
print("loading engine...")
eng = matlab.engine.start_matlab()
print("loading BPNN_Function...")
T = eng.BPNN_Function(1200,1200,
                        1, 1, 1, 1, 1, 1,#1
                        1, 1, 1, 1, 1, 1,#2
                        1, 1, 1, 1, 1, 1,#3
                        1, 1, 1, 1, 1, 1,#4
                        1, 1, 1, 1, 1, 1,#5
                        1, 1, 1, 1, 1, 1,#6
                        1, 1, 1, 1, 1, 1,#7
                        1, 1, 1, 1, 1, 1,#8
                        1, 1, 1, 1, 1, 1,#9
                        118, 90, 70, 30)


#T = [[3],[-3.0],[-0.0],[-1.0]]
print(T) #返回结果为一个矩阵 #接下来的只需要对矩阵进行处理并输出结果即可
a = [0,0,0,0]

def left_num(T,a):
    if T[3][0] == 1:
        print("左边第一单元脱胶")
        a[3] = 1
    elif T[3][0] == 3:
        print("左边第二单元脱胶")
        a[3] = 1
    elif T[3][0] == 5:
        print("左边第三单元脱胶")
        a[3] = 1
    elif T[3][0] == 4:
        print("左边第一、第二单元脱胶")
        a[3] = 2
    elif T[3][0] == 6:
        print("左边第一、第三单元脱胶")
        a[3] = 2
    elif T[3][0] == 8:
        print("左边第二、第三单元脱胶")
        a[3] = 2
    elif T[3][0] == 9:
        print("左边全部脱胶")
        a[3] = 3
    else:
        print("左边未脱胶")
        a[3] = 0


def bottom_num(T,a):
    if T[2][0] == 1:
        print("底边第一单元脱胶")
        a[2] = 1
    elif T[2][0] == 3:
        print("底边第二单元脱胶")
        a[2] = 1
    elif T[2][0] == 5:
        print("底边第三单元脱胶")
        a[2] = 1
    elif T[2][0] == 4:
        print("底边第一、第二单元脱胶")
        a[2] = 2
    elif T[2][0] == 6:
        print("底边第一、第三单元脱胶")
        a[2] = 2
    elif T[2][0] == 8:
        print("底边第二、第三单元脱胶")
        a[2] = 2
    elif T[2][0] == 9:
        print("底边全部脱胶")
        a[2] = 3
    else:
        print("底边未脱胶")
        a[2] = 0


def right_num(T,a):
    if T[1][0] == 1:
        print("右边第一单元脱胶")
        a[1] = 1
    elif T[1][0] == 3:
        print("右边第二单元脱胶")
        a[1] = 1
    elif T[1][0] == 5:
        print("右边第三单元脱胶")
        a[1] = 1
    elif T[1][0] == 4:
        print("右边第一、第二单元脱胶")
        a[1] = 2
    elif T[1][0] == 6:
        print("右边第一、第三单元脱胶")
        a[1] = 2
    elif T[1][0] == 8:
        print("右边第二、第三单元脱胶")
        a[1] = 2
    elif T[1][0] == 9:
        print("右边全部脱胶")
        a[1] = 3
    else:
        print("右边未脱胶")
        a[1] = 0

def top_num(T,a):
    if T[0][0] == 1:
        print("顶边第一单元脱胶")
        a[0] = 1
    elif T[0][0] == 3:
        print("顶边第二单元脱胶")
        a[0] = 1
    elif T[0][0] == 5:
        print("顶边第三单元脱胶")
        a[0] = 1
    elif T[0][0] == 4:
        print("顶边第一、第二单元脱胶")
        a[0] = 2
    elif T[0][0] == 6:
        print("顶边第一、第三单元脱胶")
        a[0] = 2
    elif T[0][0] == 8:
        print("顶边第二、第三单元脱胶")
        a[0] = 2
    elif T[0][0] == 9:
        print("顶边全部脱胶")
        a[0] = 3
    else:
        print("顶边未脱胶")
        a[0] = 0

left_num(T,a)
bottom_num(T,a)
right_num(T,a)
top_num(T,a)

b = (a[0]+a[1]+a[2]+a[3])/12
if b >= 0.3 and b < 0.5:
    print("玻璃处于较危险状态")
elif b>=0.5:
    print("玻璃处于严重危险状态")
else:print("玻璃处于安全状态")
