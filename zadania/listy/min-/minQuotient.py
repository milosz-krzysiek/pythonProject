from wlasne_funkcje.utils.utils_foo import generateList

def minQuotient(lista: list[int]):
    minQuotient = 100
    minQuotientIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] / lista[index + 1]
        diff = abs(diff)
        if minQuotient > diff: 
            minQuotient = diff
            minQuotientIndex = index

    return minQuotient, minQuotientIndex, minQuotientIndex+1

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = minQuotient(lista=liczby)
    print(result) 