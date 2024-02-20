#zadanie6

#czy liczby sa uporzadkowane rosnaco?

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

#np. "1 2 3", nie "1 2 1".



if((a < b) and (b < c)):
    print("kolejnosc rosnaca")
else:
    print("brak kolejnosci rosnacej")
        