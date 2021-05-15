def encrypt(w, n):
    s = ''
    for i in range(0, n-1, 2):
        s += w[i+1] + w[i]
    if n % 2 != 0:
        s += w[n-1]
    return s


w = 'marchewka'
print(encrypt(w, len(w)))

