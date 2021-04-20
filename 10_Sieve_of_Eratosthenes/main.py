import math

def sito(n):
    tab = [True] * n
    tab[0] = False
    for i in range(2, int(math.sqrt(n))+1):
        if tab[i-1]:
            for j in range(2*i-1, n, i):
                tab[j] = False
    return tab


def print_numbers(n):
    tab = []
    for i in range(1, len(n)):
        if n[i]:
            tab.append(i+1)
    return tab


print(sito(10))
print(print_numbers(sito(10)))
