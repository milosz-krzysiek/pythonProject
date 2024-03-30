import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def maxSum(lista: list[int]):
    maxSum = 10110
    maxSumIndex = 0
    n = len(lista) - 1
    for index in range(n):
        diff = lista[index] + lista[index + 1]
        diff = abs(diff)
        if maxSum > diff: 
            maxSum = diff
            maxSumIndex = index

    return maxSum, maxSumIndex, maxSumIndex+1

print(maxSum(lista=liczby))    
