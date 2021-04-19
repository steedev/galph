def dec_na_dow(n , sys):
    odwrocona_liczba = ''
    r = 1
    while r:
        r = n // sys
        c = znajdz_liczbe((n / sys - r) * sys)
        odwrocona_liczba = str(c) + odwrocona_liczba
        n = r
    return odwrocona_liczba


def znajdz_liczbe(n):
    if n <= 9:
        return int(n)
    else:
        return chr(55 + int(n))


print(dec_na_dow(141231, 16))

