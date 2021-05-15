def encrypt(w, n, k):
    k %= 26
    s = ''
    for i in range(n):
        l = ord(w[i])
        if l == 32:
            s += ' '
            continue
        if l+k > 90:
            s += chr(l+k-26)
        else:
            s += chr(l+k)
    return s

w = 'SIEMA TU KUBA'
print(encrypt(w, len(w), 92))

