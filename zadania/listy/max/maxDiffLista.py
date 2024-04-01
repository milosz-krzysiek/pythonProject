from wlasne_funkcje.utils.utils_foo import generateList


def maxDiff(lista: list[int]):
    maxDiff = 0
    maxDiffIndex = 0    
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] - lista[index + 1]
        diff = abs(diff)
        if maxDiff < diff: 
            maxDiff = diff
            maxDiffIndex = index

    return maxDiff, maxDiffIndex, maxDiffIndex+1

def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = maxDiff(lista=liczby)
    print(result)
