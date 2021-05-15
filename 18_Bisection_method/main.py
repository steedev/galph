def w_func(x):
    return x + 2

def bisection(a, b, e):
    if w_func(a) == 0:
        return a
    if w_func(b) == 0:
        return b

    while b - a > e:
        s = (a + b) / 2

        if w_func(s) == 0:
            return s

        if w_func(a) * w_func(s) < 0:
            b = s
        else:
            a = s
    return (a + b) / 2


print(bisection(-10, 10, 0.00001))
