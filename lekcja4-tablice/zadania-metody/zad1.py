def zadanie1(liszba):
    lista = []
    for x in range(1, 6):

        lista.append(x * liszba)
    return lista

def wywołanieZadania1():
    liczba = 5
    rezulat = zadanie1(liszba=liczba)
    print(rezulat)


def zadanie2(x, y):
    lista = []
    while(x < y):
        if(x % 2 == 0):
            lista.append(x)
        x = x + 1
    return lista

def wywołanieZadania2():
    liczba1 = int(input("Podaj pierwszą liczbę "))
    liczba2 = int(input("Podaj drugą liczbę "))
    rezulat = zadanie2(x = liczba1, y = liczba2)
    print(rezulat)

#wywołanieZadania1()
#wywołanieZadania2()

def zadanie3(x, y):
    lista = []
    while(x < y):
        if(x % 2 != 0):
            lista.append(x)
        x = x + 1
    lista.reverse()
    return lista

def wywołanieZadania3():
    liczba1 = int(input("Podaj pierwszą liczbę "))
    liczba2 = int(input("Podaj drugą liczbę "))
    rezulat = zadanie3(x = liczba1, y = liczba2)
    print(rezulat)

#wywołanieZadania3()
    
def zadanie4():
    pass

def wywołanieZadania4():
    pass

def zadanie5():
    pass

def wywołanieZadania5():
    pass