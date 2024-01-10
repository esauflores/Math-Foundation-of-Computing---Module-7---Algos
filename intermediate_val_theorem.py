# intermediate value theorem

import numpy as np

def ivt(a, b, f, df, tol=1e-8):
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