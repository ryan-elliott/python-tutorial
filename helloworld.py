from mymodule import person1

import platform as plat

import datetime as dt
from datetime import datetime as x

now = x.now()
print(now.year)
print(now.strftime("%A"))


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()