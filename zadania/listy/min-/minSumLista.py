from wlasne_funkcje.utils.utils_foo import generateList

def minSum(lista: list[int]):
    minSum = 10110
    minSumIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] + lista[index + 1]
        diff = abs(diff)
        if minSum > diff: 
            minSum = diff
            minSumIndex = index

    return minSum, minSumIndex, minSumIndex+1
def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = minSum(lista=liczby)
    print(result)   
