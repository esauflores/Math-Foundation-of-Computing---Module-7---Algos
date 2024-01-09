# fixed point method

import numpy as np

def fpm(x0, f, tol=1e-8, maxiter=100):
    x = x0
    iter = 0
    while iter < maxiter:
        iter+= 1
        x = f(x)
        if np.abs(x - f(x)) < tol:
            return x, iter

    return x, iter