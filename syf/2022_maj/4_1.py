p = open("przyklad.txt", 'r')
plik = [linia.strip() for linia in p]

p.close()

wynik = 0

pierwsza = "nic"



for linia in plik:

    if linia[0] == linia[-1]:

        wynik += 1

        if pierwsza == "nic":

            pierwsza = linia

print(wynik, pierwsza)

