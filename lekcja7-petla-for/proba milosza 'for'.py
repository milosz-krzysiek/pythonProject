#
#petle "for"
#

input = int(input("Podaj liczbe ,,x'', ktora nastepnie bedzie potegom liczby 2 : "))

for x in range(1, input + 1):
    print("Potegi liczby 2 to:", 2**x)