p = open("skrot.txt", 'r')

najwieksza = 0
ni_ma = 0 # tu zliczamy te co nie maja skrotu

for linia in p:

    liczba = linia.strip()
    moze_istniec = False

    for x in liczba:

        if int(x)%2 != 0:

            moze_istniec = True
            break

    if not moze_istniec:
        ni_ma += 1

        if int(liczba) > najwieksza:
            najwieksza = int(liczba)

p.close()

print(ni_ma,najwieksza)
