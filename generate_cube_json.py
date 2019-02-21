import json
import numpy as np


cube = [
    [
        { "x": 0, "y": 0, "z": z },
        { "x": 1, "y": 0, "z": z },
        { "x": 1, "y": 1, "z": z },
        { "x": 0, "y": 1, "z": z },
        { "x": 0, "y": 0, "z": z }
    ] for z in np.linspace(0, 1, 50)
]

print(json.dumps({'cube': cube}, indent=4, sort_keys=True))
