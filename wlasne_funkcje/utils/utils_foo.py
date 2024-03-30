#generowanie listy randomowych liczb w danym zakresie
import random

def generateList(start: int, end: int, number: int):
    liczby: list[int] = [random.randint(start, end) for i in range(number)]
    return liczby
