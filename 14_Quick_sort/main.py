def ustawienie_wzgledem_osi(tab, lewy, prawy):
    i = lewy - 1
    os = tab[prawy]

    for j in range(lewy, prawy):
        if tab[j] < os:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[prawy] = tab[prawy], tab[i + 1]
    return i + 1


def quick_sort(tab, lewy, prawy):
    if lewy < prawy:
        pop_index = ustawienie_wzgledem_osi(tab, lewy, prawy)

        quick_sort(tab, lewy, pop_index - 1)
        quick_sort(tab, pop_index + 1, prawy)
    return tab


tab = [2, 8, 1, 5, 4]
n = len(tab)
print(quick_sort(tab, 0, n - 1))

