from wlasne_funkcje.utils.utils_foo import generateList


def maxQuotient(lista: list[int]):
    maxQuotient = lista[0] / lista[1]
    maxQuotientIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] / lista[index + 1]
        if maxQuotient < diff: 
            maxQuotient = diff
            maxQuotientIndex = index

    return maxQuotient, maxQuotientIndex, maxQuotientIndex+1

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = maxQuotient(lista=liczby)
    print(result) 