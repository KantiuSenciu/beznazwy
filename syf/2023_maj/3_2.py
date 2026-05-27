p = open("pi.txt", 'r')



cyfry = []

for l in p:

    l = l.strip()

    cyfry.append(l)

p.close()

ilosc_wystapien = [0] * 100

for i in range(len(cyfry)-1):

    fragment = cyfry[i] + cyfry[i+1]
    j = int(fragment)
    ilosc_wystapien[j] += 1

max_wyst = max(ilosc_wystapien)
min_wyst = min(ilosc_wystapien)

print(max_wyst)
print(min_wyst)




