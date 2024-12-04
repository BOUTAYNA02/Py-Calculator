print("  Welcome to the Simple Calculator  ")
calcul  = 1
while calcul:
    print("\n New Operation ")
    first_number = input("Enter the 1st number: ")
    if first_number == 'END':
        print("END")
        calcul = 0
    else:
        operation = input("Choose the operation (+, -, *, /, **): ")
        if operation == 'quit':
            print("END")
            calcul = 0
        else:
            second_number = input("Enter the 2nd number: ")
            if second_number == 'END':
                print("END")
                calcul = 0
            else:
                if operation == '+':
                    result = float(first_number) + float(second_number)
                elif operation == '-':
                    result = float(first_number) - float(second_number)
                elif operation == '*':
                    result = float(first_number) * float(second_number)
                elif operation == '/':
                    if float(second_number) == 0:
                        print("Dividing by 0 is not possible.")
                        result = None
                    else:
                        result = float(first_number) / float(second_number)
                elif operation == '**':
                    result = float(first_number) ** float(second_number)
                else:
                    print("False operation.Try again.")
                    result = 0
                if result != 0:
                    print(f"The result is: {result}")
