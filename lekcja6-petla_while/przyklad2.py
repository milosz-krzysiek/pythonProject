#black jack, mamy podawac liczbe zeby otrzymac 23

suma_liczb = 0

while(suma_liczb != 23):
    print("Obecna suma =", suma_liczb)
    pobrana_liczba = int(input("Podaj liczbe: "))
    print()
    suma_liczb = suma_liczb + pobrana_liczba
else:
    print("BLACKJACK")
    