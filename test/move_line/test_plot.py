#@Time    :2018/11/2 16:33
import matplotlib.pyplot as plt
import random
data = [random.random() for i in range(20)]
# create an axis
ax = plt.subplot(111)

        # discards the old graph
ax.hold(False)

        # plot data
ax.plot(data, '*-')

        # refresh canvas
plt.show()