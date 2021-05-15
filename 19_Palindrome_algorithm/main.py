def palindrom(w, n):
    i = 0
    j = n
    while i < j:
        if w[i] == w[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

w = 'kuba'
print(palindrom(w, len(w) - 1))

