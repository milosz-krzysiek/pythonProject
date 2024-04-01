from zadania.listy.max.maxSumLista import maxSum
from wlasne_funkcje.utils.utils_foo import generateList



if __name__ == '__main__':
    liczby = generateList(-6, 15, 4)
    #liczby = [-1, -2, -4, -8]
    print(liczby)
    result = maxSum(lista=liczby)
#    result2 = (lista=liczby)
    print(result)

