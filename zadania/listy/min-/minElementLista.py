from wlasne_funkcje.utils.utils_foo import generateList

def findMinElement(lista: list[int]):
    min_index = 0
    for index in range(len(lista)):
        if lista[min_index] > lista[index]:
            min_index = index 
    return (lista[min_index], min_index)

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = findMinElement(lista=liczby)
    print(result) 