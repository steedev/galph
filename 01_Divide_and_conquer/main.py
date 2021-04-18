def searchMinMax(B, min, max, l, p):
    if l == p:
        if B[l] < min:
            min = B[l]
        if B[l] > max:
            max = B[l]
        return min, max

    if p - l == 1:
        if B[l] < B[p]:
            if B[l] < min:
                min = B[l]
            if B[p] > max:
                max = B[p]
        if B[l] > B[p]:
            if B[l] > max:
                max = B[l]
            if B[p] < min:
                min = B[p]
        return min, max

    s = (l + p) // 2
    min, max = searchMinMax(B, min, max, l, s)
    min, max = searchMinMax(B, min, max, s + 1, p)
    return min, max


A = [4, 3, 7, 41, 8, 44, 10, 32, 43, -3]
min = A[0]
max = A[0]

print(searchMinMax(A, min, max, 0, len(A) - 1))

