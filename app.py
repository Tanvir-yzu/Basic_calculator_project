from icecream import ic

while True:
    ic("Welcome to Calculator Project")
    ic("1. Addition")
    ic("2. Subtraction")
    ic("3. Multiplication")
    ic("4. Division")
    ic("5. Exit")

    option = int(input("Select an option for Basic Calculator Operation: "))

    if option == 5:
        ic("Exiting the calculator. Goodbye!")
        break

    if option < 1 or option > 4:
        ic("Invalid option. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == 1:
        print("    ")
        print(f"Result: {num1 + num2}")
        print("    ")
    elif option == 2:
        print("    ")
        print(f"Result: {num1 - num2}")
        print("    ")
    elif option == 3:
        print("    ")
        print(f"Result: {num1 * num2}")
        print("    ")
    elif option == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("    ")
            print(f"Result: {num1 / num2}")
            print("    ")
