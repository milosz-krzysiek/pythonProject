import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def findMaxElement(lista: list[int]):
    max = lista[0]
    for liczba in lista:
        if max < liczba:
            max = liczba

    return max

def findMaxElementIndex(lista: list[int]):
    max = findMaxElement(lista)
    index = lista.index(max)
    return index


def findMaxElement2(lista: list[int]):
    indexMax = 0

    for i in range(len(lista)):
        liczba = lista[i]
        if(lista[i] > lista[indexMax]):
            indexMax = i
    return (indexMax, lista[indexMax])
    
    


print(findMaxElement(lista=liczby))
print(findMaxElementIndex(lista=liczby))
print(findMaxElement2(lista=liczby))