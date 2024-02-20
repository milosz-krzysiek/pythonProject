#zadanie3

#czy liczba jest parzysta?

input = int(input("Podaj liczbe: "))

if(input % 2 == 0):
    print("liczba jest parzysta")
else:
    print("liczba jest nieparzysta")
    
napis = "Liczba jest"
parzystosc = ""


if(input % 2 == 0):
    parzystosc = "parzysta"
else:
    parzystosc = "nieparzysta"
    
print(napis, parzystosc)