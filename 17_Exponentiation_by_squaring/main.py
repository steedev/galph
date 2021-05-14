def potega(p, w):
    if w == 0:
        return 1
    if w % 2 == 0:
        a = potega(p, w / 2)
    else:
        return p * potega(p, w - 1)
    return a * a


print(potega(2, 5))

