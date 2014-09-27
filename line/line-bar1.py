#!/usr/bin/python
import numpy as np
import json
import matplotlib
from itertools import cycle

from matplotlib import pyplot as plt

# load settings from file
style = json.load(open("../settings1.json"))

# update matplotlib settings from file
matplotlib.rcParams.update(style)

color_cycle = matplotlib.rcParams['axes.color_cycle']

x = np.linspace(0,5,100)

# create x positions for the bar plot
a = np.arange(5)

# multiple plots in the same figure
plt.bar(a, a**2, label="Quadratic", lw=3, edgecolor=color_cycle[1], color=color_cycle[1], alpha=0.60)
plt.plot(x, x**3, label="Cubic", lw=3)

# bar plots have a width of 0.8, to center with x value ticks an adjustment is needed
plt.xticks(a+0.4, a)

# title and axis labels
plt.xlabel("Label $x$-axis")
plt.ylabel("Label $y$-axis")
plt.title("Plot title")

# legend position
plt.legend(loc="upper left")

plt.savefig("line-bar1.png")

# uncomment below to display the plot
#plt.show()
