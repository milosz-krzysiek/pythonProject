
#zad1
zmienna = input("Podaj liczbe ")

#print(zmienna, " typu ", type(zmienna))

liczba_input = int(zmienna)

liczba = liczba_input
liczba1 = liczba

#print(liczba, " typu ", type(liczba))

'''
if(liczba > 0):
    print(liczba)
else:
    liczba = liczba * (-1)
    print(liczba)
   '''

if(liczba1 < 0):
    liczba1 = liczba1 * (-1)

print("Wartosc bezwzgledna liczby: ", liczba_input, " jest rowna: ", liczba1)

