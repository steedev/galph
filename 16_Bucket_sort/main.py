def bucket_sort(A, n):
    tab = []
    K = []
    for i in range(n):
        K.append([])

    for i in range(n):
        k_i = int(A[i] * n)
        K[k_i].append(A[i])
    
    for i in range(n):
        bubble_sort(K[i], len(K[i]) - 1)

    for i in range(n):
        for j in range(len(K[i])):
            tab.append(K[i][j])
    return tab


def bubble_sort(A, n):
    for i in range(n):
        for j in range(n):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(bucket_sort(A, len(A)))

