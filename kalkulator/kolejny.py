def calculate(expression):
    operators = {'+', '-', '*', '/'}

    parts = expression.split()
    result = None
    current_operator = None

    for part in parts:
        if part in operators:
            current_operator = part
        else:
            number = float(part)
            if result is None:
                result = number
            else:
                if current_operator == '+':
                    result += number
                elif current_operator == '-':
                    result -= number
                elif current_operator == '*':
                    result *= number
                elif current_operator == '/':
                    result /= number

    return result

def multi_operation_calculator():
    while True:
        expression = input("Podaj wyrażenie matematyczne lub 'exit' aby zakończyć: ")

        if expression.lower() == 'exit':
            print("Kalkulator zakończył pracę.")
            break
