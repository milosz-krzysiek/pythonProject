
liczby = []

x = 1

while(x <= 1001):
    if(x % 3 == 0):
        #print(x)
        liczby.append(x)
    x = x + 1

suma = sum(liczby)

print(suma)    