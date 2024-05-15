#zadanie polega na znalezieniu wszystkich naturalnych dzielników liczby

def divisorsOfNumber(number: int):
    divisors : list[int] = []
    for i in range(1, number + 1):
        if(number % i == 0):
            divisors.append(i)
    return divisors

def numberIsPrime(number: int):
    if(len(divisorsOfNumber(number)) == 2):
        return True
    else:
        return False
    
def numberIsComposite(number: int):
    if(len(divisorsOfNumber(number)) > 2):
        return True
    else:
        return False