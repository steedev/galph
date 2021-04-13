def znajdz_dzielniki(n):
    d = []
    for i in range(1, n//2+1):
        if n % i == 0:
            d.append(i)
    return d


def czy_doskonala(n):
    d2 = znajdz_dzielniki(n)
    ile_d2 = len(d2)
    suma = 0
    for i in range(ile_d2):
        suma += d2[i]
    if suma == n:
        return True
    else:
        return False


print(czy_doskonala(321))

