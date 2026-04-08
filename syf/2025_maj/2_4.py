p = open("symbole.txt", 'r')
plik = [linia.strip() for linia in p]

p.close()

'''

o - 0
+ - 1
* - 2

'''
suma = 0

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

    suma += dziesietna

s = suma
suma_trojkowo = ''

while s > 0:
    suma_trojkowo = str(s%3) + suma_trojkowo
    s = s // 3

suma_symbole = ''

for znak in suma_trojkowo:

    if znak == '0':
        suma_symbole += 'o'
    elif znak == '1':
        suma_symbole += '+'
    else:
        suma_symbole += '*'


print(suma,suma_symbole)
