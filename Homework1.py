# intermediate value theorem

import numpy as np

def ivt(a, b, f, tol=1e-8, maxiter=100):
    if f(a) * f(b) > 0:
        print("f(a) and f(b) must have opposite signs")
        return None
    else:
        iter = 0
        while np.abs(b - a) > tol and iter < maxiter:
            iter+=1
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c, iter
    
# Test 1

f = lambda x: x**2 - 2

answer = np.sqrt(2)
a = 0
b = 2
tol = 1e-8
maxiter = np.Infinity

x, iter = ivt(a, b, f, tol)

print("Test 1")
print("f(x) = x^2 - 2")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")

# Test 2
    
f = lambda x: 5000 + x*(10 - 5/(1 - np.exp(-x))) - x*15

answer = 500
a = 0.1
b = 1000
tol = 0.5

x, iter = ivt(a, b, f, tol)

print("Test 2")
print("f(x) = 5000 + x*(10 - 5/(1 - np.exp(-x))) - x*15")
print("a =", a, ", b =", b)
print("x* =", x)
print("iter =", iter, ", maxiter =", maxiter)
print("anwser=", answer, ", error =", np.abs(x - answer))
print("\n")

