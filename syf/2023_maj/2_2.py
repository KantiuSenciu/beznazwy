p = open('bin_przyklad.txt','r')

max_2_bloki = []


def liczba_blokow(liczba):

    ostatnia_cyfra = liczba[0]
    licznik_blokow = 1

    for cyfra in liczba[1:]:

        if cyfra != ostatnia_cyfra:
            licznik_blokow += 1
            ostatnia_cyfra = cyfra


    return licznik_blokow

wynik = 0

for l in p:

    l = l.strip()

    if liczba_blokow(l)<=2:
        wynik+=1


print(wynik)