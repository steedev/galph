def na_dec(liczba, sys):
    wynik = 0
    potega = 0
    liczba_len = len(liczba)

    for i in range(liczba_len-1, -1, -1):
        wynik = wynik + cyfra(liczba[i]) * sys**potega
        potega += 1
    return wynik


def cyfra(n):
    if n <= '9':
        return int(n)
    else:
        return ord(str(n)) - 55


print(na_dec('1011', 2))

