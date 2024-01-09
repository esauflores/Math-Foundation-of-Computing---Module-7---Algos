# fixed point method

import numpy as np

def fpm(x0, f, tol=1e-8, maxiter=100):
    x = x0
    for _ in range(maxiter):
        x = f(x)
        if np.abs(x - f(x)) < tol:
            return x
    print("maxiter reached")
    return x


# f = lambda x: x**2 - 2
# print(fpm(2.5, f, tol=1e-10))

# f = lambda x: np.sqrt(x+2)
# print(fpm(2.5, f, tol=1e-10))

f = lambda x: 1+2/x
print(fpm(2.5, f, tol=1e-10))
