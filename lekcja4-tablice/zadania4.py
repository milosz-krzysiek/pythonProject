#zadanie zeby funkcja liczyla obwod prostokata
#i wyswietlala w ladny sposob

#poczytac o tablicach/listach w pythonie i
# sprobowac samemu odniesc sie do jej elementow

import random

bok_1 = random.randint(1, 5)
bok_2 = random.randint(2, 6)

print("Prostokat ma boki: ")
print(bok_1)
print(bok_2)

def obliczObwodProstokata(bok_1, bok_2):
    
    obwod = (bok_1 + bok_2) * 2
    #cialo funkcji
    return obwod

print("Obwod prostokata wynosi:")

print(obliczObwodProstokata(bok_1, bok_2))

def ObliczPoleProstokata(bok_1, bok_2):
    
    pole = (bok_1 * bok_2)
    
    return pole 

print("Pole prostokata wynosi:")

print(ObliczPoleProstokata(bok_1, bok_2))


#wyswietl w ladny sposob
