from wlasne_funkcje.utils.utils_foo import generateList
def minProduct(lista: list[int]):
    minProduct = 10000
    minProductIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] * lista[index + 1]
        diff = abs(diff)
        if minProduct > diff: 
            minProduct = diff
            minProductIndex = index

    return minProduct, minProductIndex, minProductIndex+1

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = minProduct(lista=liczby)
    print(result) 