def insertion_sort(tab, n):
    for i in range(1, n + 1):
        j = i
        while (j and tab[j] < tab[j - 1]):
            tab[j], tab[j - 1] = tab[j - 1], tab[j]
            j -= 1
    return tab


tab = [2, 8, 1, 5, 4]
print(insertion_sort(tab, len(tab) - 1))

