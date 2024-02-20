#zadanie 4

#najmniejsza z 3 liczb

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

print(a, b, c)

if(a > b):
    if(b > c):
        print(c)
    else:
        print(b)      
else:
    if(a > c):
        print(c)
    else:
        print(a)