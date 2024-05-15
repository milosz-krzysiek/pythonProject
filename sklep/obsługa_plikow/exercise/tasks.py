def adjustLine(line):
    #funkcja dostaje jako parametr string 'line', 
    #za zadanie ma pozbyć się '\n' z końca linii jeżeli tam się znajduje
    indeks = line.find("\n")
    if(indeks == -1):
        return line
    part1 = line[0:indeks]
    return part1

def task1():
    file = open("sklep\obsługa_plikow\exercise\dane.txt", mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")

def task2():
    file = open(input("Podaj ScieZkę:"), mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")
    
def task3(path):
    file = open(path, mode="r", encoding="utf-8")
    result = []
    for line in file:
        result.append(adjustLine(line))
    return result        

def displayTask3():
    res = task3("sklep\obsługa_plikow\exercise\dane.txt")
    print(res)

def task4(path):
    file = open(path, mode="r", encoding="utf-8")
    wordsNum = 0
    for line in file:
        words = adjustLine(line).split(sep=" ")
        length = len(words)
        wordsNum += length

    return wordsNum

def task5():
    
    
    pass    

task4("sklep\obsługa_plikow\exercise\dane.txt")
# displayTask3()