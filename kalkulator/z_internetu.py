

def kalkulator():
    while True:
        input_message = input("Podaj wyrażenie matematyczne lub 'exit' aby zakończyć: ")

        if input_message.lower() == 'exit':
            print("Kalkulator zakończył pracę.")
            break

    
        result = input_message


if __name__ == "__main__":
    kalkulator()