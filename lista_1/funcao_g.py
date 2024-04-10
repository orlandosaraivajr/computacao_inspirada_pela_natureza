import numpy as np


def g(x):
    return  2 ** (-2 * ((x - 0.1) / 0.9) ** 2)  * (np.sin(5 * np.pi * x) ) ** 6
