from configparser import LegacyInterpolation
from re import L


zmienna = True
#print(type(zmienna))

a = 7
b = 7

#sprawdz ktora jest wieksza

if(a > b):
    print("a jest wieksze")
elif(a < b):
    print("b jest wieksze")
#elif(a == b):
else:
    print("a jest rowne b")
    
'''
nieoptymalne uzycie ifa

if(a > b):
    print("a jest wieksze")
else:
    print("a nie jest wieksze")
    
if(b > a):
    print("b jest wieksze")
else:
    print("b nie jest wieksze")
    
if(b == a):
    print("a jest rowne b")
else:
    print("a nie jest rowne b")
    
    '''
    
