import numpy as np

PI = np.pi
step = 10
list = []
for i in range(0, step):
    angle = 2 * PI / step * i
    dot = np.array([np.cos(angle) * 3, np.sin(angle) * 3, 0])
    list.append(dot)
    if (i + 1) % 3 == 0:
        list.append(dot)
print(list)

dot_list = [np.array([3., 0., 0.]), np.array([2.42705098, 1.76335576, 0.]), np.array([0.92705098, 2.85316955, 0.]),
            np.array([0.92705098, 2.85316955, 0.]),
            np.array([-0.92705098, 2.85316955, 0.]),np.array([-2.42705098, 1.76335576, 0.]), np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]),
            np.array([-3.0000000e+00, 3.6739404e-16, 0.0000000e+00]), np.array([-2.42705098, -1.76335576, 0.]),
            np.array([-0.92705098, -2.85316955, 0.]), np.array([0.92705098, -2.85316955, 0.]),
            np.array([0.92705098, -2.85316955, 0.]), np.array([2.42705098, -1.76335576, 0.])]
