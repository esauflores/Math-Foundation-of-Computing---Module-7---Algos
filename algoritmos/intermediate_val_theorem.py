# intermediate value theorem

import numpy as np

def ivt(a, b, f, tol=1e-8):
    if f(a) * f(b) > 0:
        print("f(a) and f(b) must have opposite signs")
        return None
    else:
        while np.abs(b - a) > tol:
            c = (a + b) / 2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c
    

# f = lambda x: x**2 - 2
# print(intermediate_val_theorem(0, 2, f, tol=1e-10))
    
f = lambda x: 5000 + x*(10 - 5/(1 - np.exp(-x))) - x*15
print(ivt(0.1, 1000, f, tol=1e-10))