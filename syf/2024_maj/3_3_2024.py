p = open('skrot2_przyklad.txt', 'r')

wynik = []

for l in p:

    liczba = l.strip()
    skrot = ''

    for x in liczba:

        if int(x) % 2 != 0:
            skrot = skrot + x

    n = int(liczba)
    s = int(skrot)

# nwd
    while s != n:
        if s > n:
            s = s - n
        else:
            n = n - s

    if s == 7:
        wynik.append(liczba)


print(wynik)


