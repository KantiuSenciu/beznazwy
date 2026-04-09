p = open("symbole.txt", 'r')
plik = [linia.strip() for linia in p]
znaki = len(plik[0]) # liczba znaków w wierszu

p.close()

kwadraty = []

for i in range(len(plik) - 2):
    for j in range(znaki-2): # te -2 to odejmujemy bo szukamy kwadratu 3x3 wiec zeby nie wyjebalo tam nieistniejacych indeksow
        w1 = plik[i]
        w2 = plik[i+1]
        w3 = plik[i+2]

        z1 = w1[j] + w1[j+1] + w1[j+2]
        z2 = w2[j] + w2[j+1] + w2[j+2]
        z3 = w3[j] + w3[j+1] + w3[j+2]

        linia = (z1[0] == z1[1] == z1[2]) # czy w lini sa wszystkie znaki jednakowe
        kwadrat = (z1 == z2 == z3) # czy w kwadracie sa wszystkie linie jednakowe

        if linia and kwadrat:

            wspolrzedne = i+2, j+2
            kwadraty.append(wspolrzedne)



print('liczba kwadratow: ',len(kwadraty))
print('wspolrzedne srodkow:')
for wiersz,kolumna in kwadraty:
    print(wiersz,kolumna)
