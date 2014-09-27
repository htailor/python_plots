#!/usr/bin/python

"""
Demonstrates similarities between pcolor, pcolormesh, imshow and pcolorfast
for drawing quadrilateral grids.

"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context(rc={"figure.figsize": (8, 8)})

data = np.random.rand(5, 5)

data = (data + data.T)/2

print data

sns.corrplot(data, sig_tail='upper');

plt.savefig('seaborn-heatmap1.png', dpi=300)
#plt.savefig('seaborn-heatmap1.pdf')
