def anagram(w1, n1, w2, n2):
    if n1 != n2:
        return False
    A = [0] * 127
    for i in range(n1):
        A[ord(w1[i])] += 1
        A[ord(w2[i])] -= 1
    for i in range(127):
        if A[i] != 0:
            return False
    return True


w1 = 'krab'
w2 = 'bark'
print(anagram(w1, len(w1), w2, len(w2)))

