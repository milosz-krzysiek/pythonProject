def kalkulator():
    while True:
        konewka = input("Podaj wyrażenie matematyczne lub 'exit' aby zakończyć: ")

        if konewka.lower() == 'exit':
            print("Kalkulator zakończył pracę.")
            break

        try:
            result = eval(konewka)
            print("Wynik:", result)
        except Exception as e:
            print("Błąd:", e)

if __name__ == "__main__":
    kalkulator()