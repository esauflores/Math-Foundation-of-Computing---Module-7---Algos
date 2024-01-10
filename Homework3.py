# fixed point method

import numpy as np

def bisection_step(a, b, f):
    an = a; bn = b; c = (an + bn) / 2
    an, bn = (a, c) if f(a) * f(c) < 0 else (c, b)
    return an, bn, c

def bisection(a, b, f, tol=1e-8):
    iter = 0; steps = []; error = []; last = None

    while iter < maxiter:
        an, bn, c = bisection_step(a, b, f)
        if last != None: error.append(np.abs(c - last))
        steps.append(c); iter += 1; a = an; b = bn
        if np.abs(b - a) <= tol: break
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
    x0 = x; iter = 0; steps = [x0]; error = []; x1 = None
    if f(x0) == 0.0: return x0

    while iter < maxiter:
        if df(x0) != 0.0 : x1 = newton_step(x0, f, df)
        if df(x0) == 0.0 or x1 == None or x1 < a or x1 > b: a, b, x1 = bisection_step(a, b, f)
        error.append(np.abs(x1 - x0)); steps.append(x1); iter += 1
        if np.abs(x1 - x0) <= tol: break
        x0 = x1; x1 = None

    return x1, iter, steps, error

# # Test 1

# f = lambda x: (x-3)*((x-1)**2)
# df = lambda x: 3*(x)**2 - 10*x + 7

# x1 = 2
# a = -100
# b = 100
# tol = 1e-20
# maxiter = np.Infinity

# x, iter, steps_comb, error = ivt_fpn(x1, a, b, f, df, tol, maxiter)


# # print("Combined method")
# # for i in range(len(steps_comb)):
# #     print(i, "x =", steps_comb[i], ", f(x) =", f(steps_comb[i]))
# # print()

# print("Test 1")
# print("f(x) = (x-3)*((x-1)**2)")
# print("a =", a, ", b =", b)
# print("x* =", x)
# print("iter =", iter, ", maxiter =", maxiter)
# print("\n")


# # Test 2

# f = lambda x: (x-3)*((x-1)**2)
# df = lambda x: 3*(x)**2 - 10*x + 7

# x2 = -2
# a = -100
# b = 100
# tol = 1e-20
# maxiter = np.Infinity

# x, iter, steps_comb, error = ivt_fpn(x2, a, b, f, df, tol, maxiter)


# # print("Combined method")
# # for i in range(len(steps_comb)):
# #     print(i, "x =", steps_comb[i], ", f(x) =", f(steps_comb[i]))
# # print()

# print("Test 2")
# print("f(x) = (x-3)*((x-1)**2)")
# print("a =", a, ", b =", b)
# print("x* =", x)
# print("iter =", iter, ", maxiter =", maxiter)
# print("\n")


# Test 3

f = lambda x: (x-3)*((x-1)**2)
df = lambda x: 3*(x)**2 - 10*x + 7

x3 = -1
a = -100
b = 100
tol = 1e-8
maxiter = np.Infinity

x, iter, steps_comb, error = bisection_newton(x3, a, b, f, df, tol, maxiter)


print("Combined method")
for i in range(len(steps_comb)):
    print(i, "x =", steps_comb[i], ", f(x) =", f(steps_comb[i]))
print()

print("Test 3")
print("f(x) = (x-3)*((x-1)**2)")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("\n")