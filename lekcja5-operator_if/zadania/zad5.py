#zadanie5 
import math

pi = math.pi
print(pi)
#czy conajmniej 2 z 3 sa takie same?

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

'''
result = True

if(a != b):
    if(b != c):
        if(a != c):
            result = False
   '''

'''
result = False

if(a == b):
    result = True
elif(a == c):
    result = True
elif(b == c):
    result = True    

    
if(result == True):
    print("znaleziono pare")
else:
    print("brak par")
    '''
    
if( (a == b) or (b == c) or (a == c)):
    print("co najmniej jedna para")
else:
    print("brak par")    