import matlab.engine
print("loading engine...")
eng = matlab.engine.start_matlab()
print("loading input_output...")
#eng.input_output(nargout=0)
ret = eng.input_output(100)
print(ret)
