def bubble_sort(tab, n):
    for i in range(n):
        for j in range(n):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


tab = [3, -5, 2, 16, 1, 4, -2, 7]
print(bubble_sort(tab, len(tab) - 1))
