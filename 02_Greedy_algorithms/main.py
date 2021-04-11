def findBest(reszta):
    monety = [1, 2, 5]
    liczba_monet_do_wydania = 0

    while reszta:
        nominal_do_wydania = 0
        for nominal in monety:
            if (nominal <= reszta and nominal > nominal_do_wydania):
                nominal_do_wydania = nominal
        reszta -= nominal_do_wydania
        liczba_monet_do_wydania += 1
    return liczba_monet_do_wydania


print(findBest(8))
