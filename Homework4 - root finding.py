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
        if np.abs(b - a) <= tol and f(c) <= tol: break
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
        if np.abs(x1 - x0) <= tol: break
        x0 = x1

    return x0, iter, steps, error

def bisection_newton(x, a, b, f, df, tol=1e-20, maxiter=100):
    x0, iter, steps, error, x1 = x, 0, [], [], None

    while iter < maxiter:
        if df(x0) != 0.0 : x1 = newton_step(x0, f, df)
        if x1 == None or x1 < a or x1 > b: a, b, x1 = bisection_step(a, b, f)
        error.append(np.abs(x1 - x0)); steps.append(x1); iter += 1
        if np.abs(x1 - x0) <= tol and f(x1) <= tol: break
        x0 = x1; x1 = None

    return x1, iter, steps, error

# Test 1

f = lambda x: 1 - np.exp(-x)
df = lambda x: np.exp(-x)

x1 = 2
a = -1
b = 6
tol = 1e-8
maxiter = 200

steps = []

x_comb, iter_comb, steps_comb, error_comb = bisection_newton(x1, a, b, f, df, tol, maxiter)
x_ivt, iter_ivt, steps_ivt, error_ivt = bisection(a, b, f, tol)
x_fpn, iter_fpn, steps_fpn, error_fpn  = newton(x1, f, df, tol)


print("Combined method")
for i in range(len(steps_comb)):
    print(i, "x =", steps_comb[i], ", f(x) =", f(steps_comb[i]))
print()

# print("Bisection method")
# for i in range(len(steps_ivt)):
#     print(i, "x =", steps_ivt[i], ", f(x) =", f(steps_ivt[i]))
# print()    


print("Newton's method")
for i in range(len(steps_fpn)):
    print(i, "x =", steps_fpn[i], ", f(x) =", f(steps_fpn[i]))
print()    


print(error_ivt)
print(error_fpn)
print(error_comb)

# algorithm convergence plot

plt.figure(figsize=(10, 10))
plt.plot(range(len(error_ivt)), error_ivt, label="Bisection")
plt.plot(range(len(error_fpn)), error_fpn, label="Newton")
plt.plot(range(len(error_comb)), error_comb, label="Combined")
plt.xlabel("iteration")
plt.ylabel("error")
plt.legend()
plt.show()