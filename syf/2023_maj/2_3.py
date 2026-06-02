p = open('bin_przyklad.txt','r')

najwieksza = 0

for l in p:

    l = l.strip()

    if int(l) > najwieksza:
        najwieksza = int(l)


print(najwieksza)