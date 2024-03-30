
def maxProduct(lista: list[int]):
    maxProduct = lista[0] * lista[1]
    maxProductIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] * lista[index + 1]
        if maxProduct < diff: 
            maxProduct = diff
            maxProductIndex = index

    return maxProduct, maxProductIndex, maxProductIndex+1