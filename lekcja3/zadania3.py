#zadanie zeby funkcja liczyła obwód prostokąta
#i wyswietlala w ladny sposob

#poczytac o tablicach/listach w pythonie i
# sprobowac samemu odniesc sie do jej elementow


import random

bok_pierwszy = (random.randint(1, 5))
bok_drugi = (random.randint(2, 6))

def obliczObwódProstokąta(bok_pierwszy, bok_drugi):
    obwód = 2 * ( bok_pierwszy + bok_drugi)
    return obwód


def obliczObwódIŁadnieWyświelt(bok_pierwszy, bok_drugi):
    obwód = obliczObwódProstokąta(bok_pierwszy, bok_drugi)


print("Obwód prostokąta o bokach:", bok_pierwszy, "oraz", bok_drugi, "jest równe:", obwód)