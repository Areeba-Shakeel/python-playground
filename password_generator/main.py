import random
import string

print("Password Generator Started")
print("Type 'exit' anytime to quit\n")

while True:

    
    while True:
        length = input("Enter password length: ").lower()

        if length == "exit":
            print("Program ended")
            exit()

        if length.isdigit():
            length = int(length)

            if length < 4:
                print("Password should be at least 4 characters")
                continue

            break
        else:
            print("Please enter a valid number")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


    while True:
        again = input("\nDo you want another password? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break  

        elif again in ["no", "n"]:
            print("Program ended")
            exit()  

        else:
            print("Invalid input, please type yes or no")