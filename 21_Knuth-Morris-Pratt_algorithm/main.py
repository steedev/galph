def fi(w, s):
    wd, sd = len(w), len(s)
    for i in range(wd):
        if s[0] == w[i] and wd-i-sd >= 0:
            r = True
            for j in range(1, sd):
                if w[i+j] != s[j]:
                    r = False
    return r


w = 'Ala ma kota'
s = 'ma'
print(fi(w, s))

