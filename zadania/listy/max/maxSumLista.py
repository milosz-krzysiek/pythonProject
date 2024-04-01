from wlasne_funkcje.utils.utils_foo import generateList


def maxSum(lista: list[int]):
    maxSum = lista[0] + lista[1]
    maxSumIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] + lista[index + 1]
        if maxSum < diff: 
            maxSum = diff
            maxSumIndex = index

    return maxSum, maxSumIndex, maxSumIndex+1


def usage():
    liczby = generateList(1, 100, 15)
    print(liczby)
    result = maxSum(lista=liczby)
    print(result) 