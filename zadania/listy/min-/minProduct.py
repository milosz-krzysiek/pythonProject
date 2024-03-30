import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

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

print(minProduct(lista=liczby))    