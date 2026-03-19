## do skonczenia


plik = open("symbole.txt")
plik = plik.read()
znaki = 12 # liczba znaków w wierszu 


for i in range(0, len(plik) - 2):
    for j in range(0, znaki-2): # te 2 to odejmujemy bo szukamy kwadratu 3x3 wiec zeby nie wywalilo tam nieistniejacych indeksow
        w1 = plik[i]
        w2 = plik[i+1]
        w3 = plik[i+2]

        #z1 = w1[j] + w1[j+1] + w1[j+2]

        #print(z1)
