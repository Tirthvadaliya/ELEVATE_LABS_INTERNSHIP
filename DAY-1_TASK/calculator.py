def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def maincall():
    while True:
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
        choice = input("Select Operation (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {div(num1, num2)}")
                else:
                    print("Error! Division by zero is not allowed.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1 to 5).")

# Start the calculator
maincall()
