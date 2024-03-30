
from wlasne_funkcje.ujemne.max.maxProduct import maxProduct
from wlasne_funkcje.utils.utils_foo import generateList

if __name__ == '__main__':
    liczby = generateList(-11, 10, 4)
    print(liczby)
    result = maxProduct(lista=liczby)
    print(result)
