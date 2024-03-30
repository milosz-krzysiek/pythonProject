import random

liczby = [random.randint(1, 100) for i in range(15)]
print(liczby)

def findMinElement(lista: list[int]):
    min_index = 0
    for index in range(len(lista)):
        if lista[min_index] > lista[index]:
            min_index = index 
    return (lista[min_index], min_index)

print(findMinElement(lista=liczby))