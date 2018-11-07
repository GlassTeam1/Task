import matlab.engine
eng = matlab.engine.start_matlab()
#eng.triarea(nargout=0)
ret = eng.triarea(1.0,5.0)
print(ret)