# fixed point method

import numpy as np

import matplotlib.pyplot as plt

def print_equations(equations, names):
    for eq in equations:
        eqstr = ""
        for name in names:
            eqstr += str(eq[name]) + name +  (' + ' if name != names[-1] else ' = ')
        eqstr += str(eq['result'])
        print(eqstr)
    print()

def gauss_elimination(equations, names, logs = False):
    eq = equations.copy(); n = len(eq)

    print("Initial equations:")
    if logs: print_equations(eq, names)

    for i in range(n - 1):
        for j in range(i+1, n):
            if np.abs(eq[i][names[i]]) < np.abs(eq[j][names[i]]):
                eq[i], eq[j] = eq[j], eq[i]

        for j in range(i + 1, n):
            eq[j]['result'] -= eq[i]['result'] * eq[j][names[i]] / eq[i][names[i]]
            for k in range(n-1, i-1, -1):
                eq[j][names[k]] -= eq[i][names[k]] * eq[j][names[i]] / eq[i][names[i]]
        
        print("Step:", i+1)
        if logs: print_equations(eq, names)


    ans = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):
        t = sum([eq[i][names[j]] * ans[j] for j in range(i+1, n)])
        ans[i] = (eq[i]['result'] - t) / eq[i][names[i]]

    return ans

def check_ans(equations, ans, names, eps = 1e-6):
    for eq in equations:
        res = 0
        for name in names:
            res += eq[name] * ans[names.index(name)]
        if np.abs(res - eq['result']) > eps:
            return False
    return True


def test_gauss_elimination(equations):
    names = list(equations[0].keys())
    names.remove('result')

    print()

    ans = gauss_elimination(equations, names, logs=1)


    readable_ans = ""
    for name in names:
        readable_ans += name + " = " + str(ans[names.index(name)]) + ", "
    readable_ans = readable_ans[:-2]

    print("Answer: ", readable_ans)
    print("Works: ", check_ans(equations, ans, names))


tests = [
    [
        {'x1': 1, 'x2': 1,   'x3': 1,   'result': 3},
        {'x1': 2, 'x2': -1,  'x3': -1,  'result': 0},
        {'x1': 6, 'x2': -4,  'x3': 2,   'result': 4}
    ],
    
    [
        {'x1': 1, 'x2': 1,   'x3': 1,   'result': 3},
        {'x1': 0, 'x2': -3,  'x3': -3,  'result': -6},
        {'x1': 0, 'x2': -10,  'x3': -4,   'result': -14}
    ],

    [
        {'x1': 1, 'x2': 1,   'x3': 1,   'result': 3},
        {'x1': 0, 'x2': -3,  'x3': -3,  'result': -6},
        {'x1': 0, 'x2': 0,  'x3': 6,   'result': 6}
    ],
]

print("Select test between 1 and", len(tests))
test = int(input()) - 1
# # test = 0
print("Test ", test + 1, ":")
test_gauss_elimination(tests[test])