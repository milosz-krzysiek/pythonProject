def wywolanie_kalkulatora():
    liczba_1 = 0
    liczba_2 = 0
    znak = ''

    #TODO czy jest liczba
    liczba_1 = int(input("Podaj liczbe pierwsza: "))
    znak = input("Podaj znak: ")
    liczba_2 = int(input("Podaj liczbe druga: "))

    if(znak == "+"): 
        wynik = liczba_1 + liczba_2
    elif(znak == "-"):
        wynik = liczba_1 - liczba_2
    elif(znak == "*"):
        wynik = liczba_1 * liczba_2
    elif(znak == "/"):
        if(liczba_2 == 0):
            print("nie można dzielić przez '0'")
            exit()        
        else:
            wynik = liczba_1 / liczba_2
    elif(znak == "**"):
        wynik = liczba_1 ** liczba_2 
        
    print(wynik)

wywolanie_kalkulatora()