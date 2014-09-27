#!/usr/bin/python
import json
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

'''
	Demonstrates how to fill simple line plots from the returned list of lines 
'''

# load settings from file
style = json.load(open("../settings1.json"))

# update matplotlib settings from file
matplotlib.rcParams.update(style)

x = np.linspace(0,5,100)

# multiple plots in the same figure, plt.plot returns a list of lines
line, = plt.plot(x, x**2, label="Quadratic", lw=3)
plt.fill_between(x, x**2, alpha=.5, facecolor=[line.get_color()])

line, = plt.plot(x, x**3, label="Cubic", lw=3)
plt.fill_between(x, x**3, alpha=.5, facecolor=[line.get_color()])

line, = plt.plot(x, np.exp(x), label="Exponential", lw=3)
plt.fill_between(x, np.exp(x), alpha=.5, facecolor=[line.get_color()])

# title and axis labels
plt.xlabel("Label $x$-axis")
plt.ylabel("Label $y$-axis")
plt.title("Plot title")

# legend position
plt.legend(loc="upper left")

plt.savefig("line2.png")

# uncomment below to display the plot
# plt.show()
