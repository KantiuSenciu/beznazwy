p = open("symbole.txt", 'r')
plik = [linia.strip() for linia in p]

p.close()

'''

o - 0
+ - 1
* - 2

'''
najwieksza = 0
odpowiednik = '' # te znaczki co odpowiadaja najwiekszej liczbie

for linia in plik:

    napis = linia.strip()

    trojkowy = ''

    for znak in linia:


        if znak == 'o':
            trojkowy += '0'
        elif znak == '+':
            trojkowy += '1'
        else:
            trojkowy += '2'

    dziesietna = int(trojkowy, 3)

    if dziesietna > najwieksza:
        najwieksza = dziesietna
        odpowiednik = napis

print(najwieksza,odpowiednik)




