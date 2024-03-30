import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def minQuotient(lista: list[int]):
    minQuotient = 100
    minQuotientIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] / lista[index + 1]
        diff = abs(diff)
        if minQuotient > diff: 
            minQuotient = diff
            minQuotientIndex = index

    return minQuotient, minQuotientIndex, minQuotientIndex+1

print(minQuotient(lista=liczby))  