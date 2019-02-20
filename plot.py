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
import json

with open('data.json') as f:
    data = json.load(f)

'''
for key in data:
    for list_inner in data[key]:
        if 1 != len(set([i["z"] for i in list_inner])):
            print(key)
            print(list_inner)
'''

for structure_name, structure in data.items():
    for contour in structure:
        if 1 != len(set([point["z"] for point in contour])):
            raise ValueError("Points in contour have different z values.")

"""
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot a sin curve using the x and y axes.
for z in range(0, 50):
    x = np.linspace(0, 1, 100)
    y = z * np.sin(x * 2 * np.pi) / 50 / 2 + 0.5
    ax.plot(x, y, zs=z, zdir='z', label='')
"""

"""
# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 50)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35)
"""

plt.show()
