from my_utils.utils import simplify_output

def wywolanie_kalkulatora(rownanie):
    liczba_1 = 0
    liczba_2 = 0
    znak = ''

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
                return "błąd"
            else:
                wynik = liczba_1 / liczba_2
        case '**':
            wynik = liczba_1 ** liczba_2
        case _:
            print("Błędny znak")
            return "błąd"
    
    return wynik

#print(simplify_output(wynik))

def kalkulator():
    while True:
        input_message = input("Podaj wyrażenie matematyczne lub 'exit' aby zakończyć: ")

        if input_message.lower() == 'exit':
            print("Kalkulator zakończył pracę.")
            break

    
        result = wywolanie_kalkulatora(input_message)

        if (result == "błąd"):
            continue
        
        print(input_message, "=", simplify_output(result))




if __name__ == "__main__":
    kalkulator()