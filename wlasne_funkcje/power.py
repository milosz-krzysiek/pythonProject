from math import pow

print(pow(3, 5))

def my_power(a, b):
    #oblicz a do potegi b
    wynik = 1 
    for x in range(1, b + 1):
        wynik = a * wynik

    return wynik

def my_power_while(a, b):
    wynik = 1
    while(b > 0):
        wynik = wynik * a
        b = b - 1
    return wynik

wynik_1 = my_power_while(3,5)
print(wynik_1, "z while")
wynik = my_power(3,5)
print(wynik, "z for", sep = ", ")
