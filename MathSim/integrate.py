import cupy as cp
import numpy as np
from scipy import stats
from .sampling import sample_from
# limits: [(x_min, x_max), (y_min, y_max), (z_min, z_max), ...]


def integrate_mc_gpu(func, limits, num):
    xs = sample_from(limits, num, cp.random.uniform)
    ys = func(xs)

    integral = cp.prod(cp.array([i[1] - i[0]
                                 for i in limits])) * cp.sum(ys) / num
    return integral


def integrate_mc_cpu(func, limits, num):
    xs = sample_from(limits, num, np.random.uniform)
    ys = func(xs)

    integral = cp.prod(cp.array([i[1] - i[0]
                                 for i in limits])) * cp.sum(ys) / num
    return integral
