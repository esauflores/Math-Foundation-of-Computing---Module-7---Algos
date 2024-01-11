# fixed point method

import numpy as np

def fpm(x0, f, tol=1e-8, maxiter=100):
    x = x0
    iter = 0
    while np.abs(x - f(x)) < tol and iter < maxiter:
        iter+= 1
        x = f(x)

    return x, iter

# Homework 2 
# Please, implement fixed point method and test it for square root function,
# and also for "modified x^2-4" with alpha parameter. 
# Experiment with it also to see, how it influences number of iterations!

# Test 1
f = lambda x: np.sqrt(x)

answer = 1
x0 = 1607
tol = 1e-8
maxiter = np.Infinity

x, iter = fpm(x0, f, tol, maxiter)
print("Test 1")
print("f(x) = sqrt(x)")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")

# Test 2
f = lambda x: np.sqrt(x)

answer = 1
x0 = 100000
tol = 1e-8
maxiter = 10

x, iter = fpm(x0, f, tol, maxiter)
print("Test 2")
print("f(x) = sqrt(x)")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")

# Test 3
f = lambda x: np.sqrt(x)

answer = 1
x0 = 10000
tol = 1e-3
maxiter = 100

x, iter = fpm(x0, f, tol, maxiter)
print("Test 3")
print("f(x) = sqrt(x)")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")

# Test 4
f = lambda x: x**2 - 4

alpha = -0.0001
g = lambda x: alpha * f(x) + x

answer = 2
x0 = 5
tol = 1e-8
maxiter = np.Infinity

x, iter = fpm(x0, g, tol, maxiter)
print("Test 4")
print("f(x) = x^2 - 4")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")


# Test 5
f = lambda x: x**2 - 4

alpha = -0.0000001
g = lambda x: alpha * f(x) + x

answer = 2
x0 = 10
tol = 1e-8
maxiter = np.Infinity

x, iter = fpm(x0, g, tol, maxiter)
print("Test 5")
print("f(x) = x^2 - 4")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")


# Test 6
f = lambda x: x**2 - 4

alpha = -0.001
g = lambda x: alpha * f(x) + x

answer = 2
x0 = 100
tol = 1e-8
maxiter = np.Infinity

x, iter = fpm(x0, g, tol, maxiter)
print("Test 6")
print("f(x) = x^2 - 4")
print("x0 =", x0, ", x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")
