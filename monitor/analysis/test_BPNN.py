import matlab.engine
print("loading engine...")
eng = matlab.engine.start_matlab()
print("loading BPNN_Function...")
ret = eng.BPNN_Function(1,1,
                        1, 1, 1, 1, 1, 1,#1
                        1, 1, 1, 1, 1, 1,#2
                        1, 1, 1, 1, 1, 1,#3
                        1, 1, 1, 1, 1, 1,#4
                        1, 1, 1, 1, 1, 1,#5
                        1, 1, 1, 1, 1, 1,#6
                        1, 1, 1, 1, 1, 1,#7
                        1, 1, 1, 1, 1, 1,#8
                        1, 1, 1, 1, 1, 1,#9
                        1, 1, 1, 1)


print(ret) #返回结果为一个矩阵
        #接下来的只需要对矩阵进行处理并输出结果即可