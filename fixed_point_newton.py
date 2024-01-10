# fixed point newton

import numpy as np

def fpn(x0, f, df, tol=1e-8, maxiter=100):
    x = x0
    iter = 0
    iters_history = []

    while np.abs(f(x)/df(x)) > tol and iter < maxiter:
        iter+= 1
        iters_history.append(x)
        x = x - f(x) / df(x)
    
    return x, iter, iters_history

# Test 1

f = lambda x: np.cos(x) - 1
df = lambda x: -np.sin(x)

x0 = 3
tol = 1e-8
maxiter = np.Infinity

x, iter, iters_history = fpn(x0, f, df, tol)

print("Test 1")
print("f(x) = cos(x) - 1")
print("tol =", tol)
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("\n")


# Test 2

f = lambda x: np.cos(x) - 1
df = lambda x: -np.sin(x)

x0 = 0.1
tol = 1e-8
maxiter = np.Infinity

x, iter, iters_history = fpn(x0, f, df, tol)

print("Test 2")
print("f(x) = cos(x) - 1")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("\n")


# Test 3

f = lambda x: np.cos(x) - 1
df = lambda x: -np.sin(x)

x0 = -1
tol = 1e-8
maxiter = np.Infinity

x, iter, iters_history = fpn(x0, f, df, tol)

print("Test 3")
print("f(x) = cos(x) - 1")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("\n")

# Test 4

f = lambda x: x**2 - 4
df = lambda x: 2*x

x0 = 50
tol = 1e-6
maxiter = np.Infinity

x, iter, iters_history = fpn(x0, f, df, tol)

print("Test 4")
print("f(x) = x^2 - 4")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("iters_history =", iters_history)
print("\n")