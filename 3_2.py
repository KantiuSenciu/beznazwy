## ni dziala ale sie nie wyspalam ale robie commitaa

p = open("skrot_przyklad.txt", 'r')

najwieksza = 0
ni_ma = 0# tu zliczamy te co nie maja skrotu

for linia in p:

    liczba = linia.strip()

    nie_moze_istniec = False

    for x in liczba:

        x = int(x)

        if x%2 != 0:

            nie_moze_istniec = True

            if nie_moze_istniec:
                ni_ma += 1

                if int(liczba) > najwieksza:
                    najwieksza = int(liczba)

            break


p.close()


print(ni_ma,najwieksza)

