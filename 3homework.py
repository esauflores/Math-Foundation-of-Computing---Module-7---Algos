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
        if np.abs(b - a) <= tol or np.abs(f(c)) <= tol: break
        last = c

    return c, iter, steps, error


def newton_step(x, f, df):
    return x - f(x) / df(x)

def newton(x, f, df, tol=1e-8, maxiter=100):
    x0 = x; iter = 0; steps = [x0]; error = []

    if df(x0) == 0.0: return None
    if f(x0) == 0.0: return x0

    while iter < maxiter:
        x1 = newton_step(x0, f, df)
        error.append(np.abs(x1 - x0)); steps.append(x1); iter += 1 
        if np.abs(x1 - x0) <= tol or np.abs(f(x1)) <= tol : break
        x0 = x1

    return x0, iter, steps, error

def bisection_newton(x, a, b, f, df, tol=1e-20, maxiter=100):
    x0, iter, steps, error, x1 = x, 0, [], [], None


    while iter < maxiter:

        if df(x0) != 0.0 : x1 = newton_step(x0, f, df)

        if x1 == None or x1 <= a or x1 >= b: a, b, x1 = bisection_step(a, b, f)
        a, b = (a, x1) if f(a) * f(x1) < 0 else (x1, b)

        error.append(np.abs(x1 - x0)); steps.append(x1); iter += 1
        if np.abs(x1 - x0) <= tol or np.abs(f(x1)) <= tol: break
        x0 = x1; x1 = None

    return x1, iter, steps, error

# tests for bisection
f, df = lambda x: (x-3) * (x-1)**2, lambda x: 3*x**2 - 10*x + 7

tol = 1e-8; maxiter = 100

# test in form [x, a, b]
tests = [[2, -100, 100], [-2, -1000, 1000], [-1, -5, 5]]


for test, i in zip(tests, range(len(tests))):
    x, a, b = test
    xr, iter, steps, error = bisection_newton(x, a, b, f, df, tol, maxiter)
    print("Test ", i + 1, ": root ", xr, " found in ", iter, " iterations")