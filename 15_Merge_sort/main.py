def merge_sort(tab, lewy, prawy):
    if lewy == prawy:
        return

    srodek = (lewy + prawy) // 2
    merge_sort(tab, lewy, srodek)
    merge_sort(tab, srodek + 1, prawy)
    merge(tab, lewy, prawy, srodek)
    return tab
    

def merge(tab, lewy, prawy, srodek):
    el_lewe = tab[lewy:srodek + 1]
    el_prawe = tab[srodek + 1:prawy + 1]

    id_lewy_pod = 0
    id_prawy_pod = 0
    id_sorted_el = lewy

    while (id_lewy_pod < len(el_lewe) and id_prawy_pod < len(el_prawe)):
        if el_lewe[id_lewy_pod] < el_prawe[id_prawy_pod]:
            tab[id_sorted_el] = el_lewe[id_lewy_pod]
            id_lewy_pod += 1
        else:
            tab[id_sorted_el] = el_prawe[id_prawy_pod]
            id_prawy_pod += 1
        id_sorted_el += 1

    while id_lewy_pod < len(el_lewe):
        tab[id_sorted_el] = el_lewe[id_lewy_pod]
        id_lewy_pod += 1
        id_sorted_el += 1

    while id_prawy_pod < len(el_prawe):
        tab[id_sorted_el] = el_prawe[id_prawy_pod]
        id_prawy_pod += 1
        id_sorted_el += 1


tab = [2, 8, 1, 5, 4]
print(merge_sort(tab, 0, len(tab) - 1))

