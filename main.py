from zadania.liczby.dzielniki_liczby import divisorsOfNumber, numberIsPrime, numberIsComposite
from wlasne_funkcje.utils.utils_foo import generateList



if __name__ == '__main__':
    liczby : list[int] = generateList(6, 15, 1)
    #liczby = [-1, -2, -4, -8]
    #liczba = 4365645
    print(liczby)
    result = divisorsOfNumber(liczby=liczby)
    result2 = numberIsPrime(liczby=liczby)
    result3 = numberIsComposite(liczby=liczby)
    print(result, result2, ",", result3)

