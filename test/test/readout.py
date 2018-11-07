#@Time    :2018/11/1 15:05
import serial
import time
import sys
from pylab import *
from numpy import *
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

# Main parameters
mesurements = 1000000
dataArray = []
timeArray = []
space = "	"
locations = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3']


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def plotsettings():
    plt.title(r'Input from arduino serial port')
    xlabel(r'$\Delta T$, $[S]$')
    ylabel(r'$Value$')


for device in locations:
    try:
        arduino = serial.Serial(device, 9600)
        print
        "Connected whith device", device
        time.sleep(0.001)
    except:
        print
        "No device at", device

text_file = open("Output.txt", "w")

# Makes 50 mesurements to make shure all mesurements are correct.
print
"Starting communication"
for i in range(0, 50):
    data = arduino.readline()

start = time.time()

for i in range(0, mesurements):
    # arduino.write('Y')
    current = time.time()
    data = arduino.readline()
    number = is_number(data)

    if number == True:
        dataArray.append(data)
        elapsed = current - start
        timeArray.append(elapsed)
        save = str(elapsed) + str(space) + str(data)
        text_file.write(save)
        print(save)
    else:
        print("Bad Data!")
        i -= 1

text_file.close()
plot(timeArray, dataArray)
plotsettings()
show()
print("End of program")
sys.exit()