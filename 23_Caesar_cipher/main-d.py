def decrypt(w, n, k):
    k %= 26
    s = ''
    for i in range(n):
        l = ord(w[i])
        if l == 32:
            s += ' '
            continue
        if l-k < 65:
            s += chr(l-k+26)
        else:
            s += chr(l-k)
    return s


w = 'GWSAO HI YIPO'
print(decrypt(w, len(w), 92))

