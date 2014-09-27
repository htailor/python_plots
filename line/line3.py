#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

'''
	Uses the plot styles avaliable in version 0.14
'''

# set plot style
#plt.style.use('bmh')
plt.style.use('ggplot')

x = np.linspace(0,5,100)

# multiple plots in the same figure
plt.plot(x, x**2, label="Quadratic", lw=3)
plt.plot(x, x**3, label="Cubic", lw=3)
plt.plot(x, np.exp(x), label="Exponential", lw=3)

# title and axis labels
plt.xlabel("Label $x$-axis")
plt.ylabel("Label $y$-axis")
plt.title("Plot title")

# legend position
plt.legend(loc="upper left")

plt.savefig("line3.png")

# uncomment below to display the plot
# plt.show()
