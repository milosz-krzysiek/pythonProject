def wczytajDane():
    file = open("sklep\obsługa_plikow\cennik", mode="r", encoding="utf-8")
    print(file)
    tresc = file.read(3)
    tresc2 = file.read()
    print(tresc)
    print()
    print(tresc2)
    print()
    tresc3 = file.read()
    print(tresc3)

def przeczytajPlikLiniami():
    file = open("sklep\obsługa_plikow\cennik", mode="r", encoding="utf-8")

    for line in file:
        print(line, end="")

    

if __name__ == '__main__':
    przeczytajPlikLiniami()
    # wczytajDane()
