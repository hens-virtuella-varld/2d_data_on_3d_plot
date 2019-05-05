# 2d_data_on_3d_plot
A Python open source project visualizes 2D JSON data on 3D plot.

This project's purpose was to visualize DICOM-RT data.

## Requirements
- Python 3

## Setup
```
$ git clone https://github.com/hens-virtuella-varld/2d_data_on_3d_plot.git
$ cd 2d_data_on_3d_plot
(create and activate virtual environment if needed)
$ pip install -r requirements.txt
```

## Execution
```
$ python generate_cube_json.py > sample.json # This generates a sample data.
$ python plot.py sample.json cube
```
## JSON and plot example
An example of cube composed of 3 squares.

```
{
  "cube": [
    [
      { "x": 0, "y": 0, "z": 0.0 },
      { "x": 1, "y": 0, "z": 0.0 },
      { "x": 1, "y": 1, "z": 0.0 },
      { "x": 0, "y": 1, "z": 0.0 },
      { "x": 0, "y": 0, "z": 0.0 }
    ],
    [
      { "x": 0, "y": 0, "z": 0.5 },
      { "x": 1, "y": 0, "z": 0.5 },
      { "x": 1, "y": 1, "z": 0.5 },
      { "x": 0, "y": 1, "z": 0.5 },
      { "x": 0, "y": 0, "z": 0.5 }
    ],
    [
      { "x": 0, "y": 0, "z": 1.0 },
      { "x": 1, "y": 0, "z": 1.0 },
      { "x": 1, "y": 1, "z": 1.0 },
      { "x": 0, "y": 1, "z": 1.0 },
      { "x": 0, "y": 0, "z": 1.0 }
    ]
  ]
}

```
![sample cube](cube.png)

## License
Copyright (c) 2019 [hens-virtuella-varld](https://github.com/hens-virtuella-varld)

The project is licensed under the MIT License. 

## Contact
### Regan Y.
E-mail: hens.virtuella.varld@gmail.com  
LinkedIn: https://www.linkedin.com/in/regan-y/  
I will be happy to talk to you if you have any advices to my project.
