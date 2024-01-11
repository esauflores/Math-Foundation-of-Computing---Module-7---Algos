# fixed point method

import numpy as np

import matplotlib.pyplot as plt

def bisection_step(a, b, f):
    an, b, c = a, b, (a + b) / 2
    an, bn = (a, c) if f(a) * f(c) < 0 else (c, b)
    return an, bn, c

def bisection(a, b, f, tol=1e-8):
    iter, steps, error, last = 0, [], [], None

    while iter < maxiter:
        an, bn, c = bisection_step(a, b, f)
        if last != None: error.append(np.abs(c - last))
        steps.append(c); iter, a, b = iter + 1, an, bn
        if np.abs(b - a) <= tol: break
        last = c

    return c, iter, steps, error

def newton_step(x, f, df):
    return x - f(x) / df(x)

def newton(x, f, df, tol=1e-8, maxiter=100):
    x0 = x; iter = 0; steps = [x0]; error = []

    while iter < maxiter:
        x1 = newton_step(x0, f, df)
        error.append(np.abs(x1 - x0)); steps.append(x1); iter += 1 
        if np.abs(x1 - x0) <= tol: break
        x0 = x1

    return x0, iter, steps, error

def bisection_newton(x, a, b, f, df, tol=1e-20, maxiter=100):
    x0, iter, steps, x1 = x, 0, [x0], None

    while iter < maxiter:
        if df(x0) != 0.0 : x1 = newton_step(x0, f, df)

        if x1 == None or x1 <= a or x1 >= b: 
            a, b, x1 = bisection_step(a, b, f)
            if b - a <= tol: break
        else: 
            a, b = (a, x1) if f(a) * f(x1) < 0 else (x1, b)
            if np.abs(x1 - x0) <= tol: break

        steps.append(x1); iter += 1; x0 = x1; x1 = None

    return x1, iter, steps


# tests for bisection
f, df = lambda x: 1 - np.exp(-x), lambda x: np.exp(-x)

tol = 1e-8; maxiter = 100

# test in form [x, a, b]
test = [4.5, -1, 5]

x, a, b = test
xr, iter, steps = bisection_newton(x, a, b, f, df, tol, maxiter)
xr, iter, steps = newton(x, f, df, tol, maxiter)

print("Bisection Newton: ", xr, iter)

for i in range(len(steps)):
    print("step ", i , steps[i])

print()

print("Newton: ", xr, iter)

for i in range(len(steps2)):
    print("step ", i, steps2[i])


print(xr, f(xr))




plt.figure(figsize=(10, 10))
plt.plot(range(len(error2)), error2, label="Newton")
plt.plot(range(len(error)), error, label="Combined")
plt.xlabel("iteration")
plt.ylabel("error")
plt.yscale("log")
plt.legend()
plt.show()