"""
=======================
Plot 2D data on 3D plot
=======================

Demonstrates using ax.plot's zdir keyword to plot 2D data on
selective axes of a 3D plot.
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import sys
import json


data_file = sys.argv[1]
structure_name = sys.argv[2]
color = sys.argv[3] if len(sys.argv) == 4 else 'grey'

with open(data_file) as f:
    data = json.load(f)

fig = plt.figure()
ax = fig.gca(projection='3d')

for contour in data[structure_name]:
    if 1 != len(set([point["z"] for point in contour])):
        raise ValueError("Points in contour have different z values.")
    z = contour[0]["z"]
    x = []
    y = []
    for point in contour:
        x.append(point["x"])
        y.append(point["y"])
    ax.plot(x, y, zs=z, zdir='z', color=color)

plt.show()
