from my_utils.utils import simplify_output

liczba_1 = 0
liczba_2 = 0
znak = ''

rownanie = input("Podaj równanie do rozwiązania, oddzielaj wszystko spacją:\n")
rownanie = rownanie.split()

liczba_1 = float(rownanie[0])
znak = rownanie[1]
liczba_2 = float(rownanie[2])

match znak:
    case '+':
        wynik = liczba_1 + liczba_2
    case '-':
        wynik = liczba_1 - liczba_2
    case '*':
        wynik = liczba_1 * liczba_2
    case '/':
        if(liczba_2 == 0):
            print("Nie dziel przez '0'")
            exit()
        else:
            wynik = liczba_1 / liczba_2
    case _:
        print("Błędny znak")
        exit()

print(simplify_output(wynik))