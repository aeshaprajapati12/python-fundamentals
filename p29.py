num1 = int(input("Enter a number1 : "))
num2 = int(input("Enter a number2 : "))
choice = input("Enter a choice (+,-,*,/) : ")

match choice:
    case '+':
        print("Addition is = " , num1 + num2)

    case '-':
        print("Substraction is = " , num1 - num2)

    case '*':
        print("Muliplication is = " , num1 * num2)

    case '/':
        print("Division is = " , num1 / num2)
        
    case _:
        print("Invalid number")