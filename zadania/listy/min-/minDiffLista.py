from wlasne_funkcje.utils.utils_foo import generateList

def minDiff(lista: list[int]):
    minDiff = 100
    minDiffIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] - lista[index + 1]
        diff = abs(diff)
        if diff < minDiff:
            minDiff = diff
            minDiffIndex = index

    return minDiff, minDiffIndex, minDiffIndex + 1

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = minDiff(lista=liczby)
    print(result) 