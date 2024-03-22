import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

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

print(maxDiff(lista=liczby))