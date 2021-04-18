def euklides_rekur(a, b):
    if b != 0:
        return euklides_rekur(b, a%b)
    return a


print(euklides_rekur(24, 18))
