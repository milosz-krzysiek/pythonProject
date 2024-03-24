import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def maxProduct(lista: list[int]):
    maxProduct = 1
    maxProductIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] * lista[index + 1]
        diff = abs(diff)
        if maxProduct < diff: 
            maxProduct = diff
            maxProductIndex = index

    return maxProduct, maxProductIndex, maxProductIndex+1

print(maxProduct(lista=liczby))    