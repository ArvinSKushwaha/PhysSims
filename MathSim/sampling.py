import cupy as cp
import numpy as np

def sample_from(limits, num, sample_func):
    xs = sample_func(size=(num, len(limits)))
    for i in range(len(limits)):
        lim = limits[i]
        xs[:, i] = xs[:, i] * (lim[1] - lim[0]) + lim[0]

    return xs