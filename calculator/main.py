print("Simple Calculator Started")

while True:

    print("\nChoose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Calculator closed")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

    
    while True:
        again = input("\nDo you want to continue? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break   

        elif again in ["no", "n"]:
            print("Calculator ended")
            exit()

        else:
            print("Invalid input, please type 'yes' or 'no'")