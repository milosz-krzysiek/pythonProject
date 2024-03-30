from wlasne_funkcje.utils.utils_foo import generateList

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
    
    
def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    print(findMaxElement(lista=liczby))
    print(findMaxElementIndex(lista=liczby))
    print(findMaxElement2(lista=liczby))