plik = open("symbole.txt")

for wiersz in plik:
    wiersz = wiersz.strip()

    i = 0
    j = len(wiersz) - 1

    palindrom = True

    while i < j:
        if wiersz[i] != wiersz[j]:
            palindrom = False
            break
        else:
            i += 1
            j -= 1

    if palindrom:
        print(wiersz)
