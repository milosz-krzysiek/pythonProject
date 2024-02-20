import random
czy_Mati_to_cymbał = False


# print(type(czy_Mati_to_cymbał))yes

def sprawdzanieMateusz(czy_Mati_to_cymbał):
    if (czy_Mati_to_cymbał == True):
        print("Mati cymbale wez sie za nauke")
    else:
        print("Mati jest mondry")


def policzPoleProstokąta(bok_pierwszy, bok_drugi):
    pole = bok_pierwszy * bok_drugi
    return pole


def policzPoleIŁadnieWyswietl(bok_pierwszy, bok_drugi):
    pole = policzPoleProstokąta(bok_pierwszy, bok_drugi)
    print("Pole prostokata o bokach: ", bok_pierwszy, " oraz ", bok_drugi, " jest rowne: ", pole)


# policzPoleIŁadnieWyswietl(2, 3)

liczba = (random.randint(1, 10))
print(liczba)
if(liczba == 1):
    print("wygrales loterie")
elif(liczba == 5):
    print("piontka")
elif(liczba > 7):
    print("ulallal brahu duza liczba")
else:
    print("sory taki mam klimat")