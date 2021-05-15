def anagram(w1, n1, w2, n2):
    if n1 != n2:
        return False
    q1 = 0
    for i in range(n1):
        q1 += ord(w1[i])
        q1 -= ord(w2[i])
    if q1 != 0:
        return False
    return True


w1 = 'rabk'
w2 = 'bark'
print(anagram(w1, len(w1), w2, len(w2)))

