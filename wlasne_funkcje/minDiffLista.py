import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

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

print(minDiff(lista=liczby))