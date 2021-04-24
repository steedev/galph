def selection_sort(tab, n):
    for i in range(n):
        min=i
        for j in range(i + 1, n + 1):
            if tab[min] > tab[j]:
                min=j
        tab[min], tab[i] = tab[i], tab[min]
    return tab


tab = [2, 8, 1, 5, 4]
print(selection_sort(tab, len(tab) - 1))

