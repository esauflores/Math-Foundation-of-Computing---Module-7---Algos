# fixed point method

import numpy as np

def ivt_fpn(x0, a, b, f, df, tol=1e-8, maxiter=100, steps= []):
    if f(a) * f(b) > 0:
        return None
    
    steps.append(x0)

    dx = df(x0)
    if dx != 0.0:
        x1 = x0 - f(x0) / dx
        if np.abs(x1 - x0) < tol: 
            steps.append(x1)
            return x1, 0, steps

        if b <= x1 and x1 <= a:
            if f(x1) * f(a) < 0: b = x1
            else: a = x1
            x, iter, steps = ivt_fpn(x1, a, b, f, df, tol, maxiter, steps)
            return x, iter+1, steps
        
    if np.abs(b - a) < tol:
        steps.append((a+b)/2)
        return c, 0, steps
    
    c = (a + b) / 2
    if f(c) * f(a) < 0: b = c
    else: a = c
    
    x, iter, steps = ivt_fpn(c, a, b, f, df, tol, maxiter, steps)
    return x, iter+1, steps

# Test 1

f = lambda x: (x-3)*((x-1)**2)
df = lambda x: 3*(x-1)**2 - 10*x + 7

x1 = 2
a = -100
b = 100
tol = 1e-8
maxiter = np.Infinity

steps = []
x, iter, steps = ivt_fpn(x1, a, b, f, df, tol, maxiter)

print("Test 1")
print("f(x) = (x-3)*((x-1)**2)")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("steps =", steps)
print("\n")


# Test 2

f = lambda x: (x-3)*((x-1)**2)
df = lambda x: 3*(x-1)**2 - 10*x + 7

x2 = -2
a = -100
b = 100
tol = 1e-8
maxiter = np.Infinity


steps = []
x, iter, steps = ivt_fpn(x2, a, b, f, df, tol, maxiter, steps)

print("Test 2")
print("f(x) = (x-3)*((x-1)**2)")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("steps =", steps)
print("\n")


# Test 3

f = lambda x: (x-3)*((x-1)**2)
df = lambda x: 3*(x-1)**2 - 10*x + 7

x3 = -1
a = -100
b = 100
tol = 1e-8
maxiter = np.Infinity

steps = []
x, iter, steps = ivt_fpn(x3, a, b, f, df, tol, maxiter, steps)

print("Test 3")
print("f(x) = (x-3)*((x-1)**2)")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("steps =", steps)
print("\n")
