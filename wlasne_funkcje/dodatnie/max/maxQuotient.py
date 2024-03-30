import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def maxQuotient(lista: list[int]):
    maxQuotient = 1
    maxQuotientIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] / lista[index + 1]
        diff = abs(diff)
        if maxQuotient < diff: 
            maxQuotient = diff
            maxQuotientIndex = index

    return maxQuotient, maxQuotientIndex, maxQuotientIndex+1

print(maxQuotient(lista=liczby))  