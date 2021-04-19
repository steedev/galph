def rozklad(n):
    i = 2
    A = []
    while (n > 1 and i*i <= n):
        while n % i == 0:
            A.append(i)
            n //= i
        i += 1
    if n > 1:
        A.append(n)
    return A


print(rozklad(28))

