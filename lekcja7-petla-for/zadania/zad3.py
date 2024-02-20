
input = int(input("Podaj liczbe 'x' : "))
suma = 0

for x in range(1, input + 1):
    element = x**2
    suma = suma + element
    
print(suma)