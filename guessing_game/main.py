import random

print("Guessing Game Started")

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Type 'exit' anytime to quit the game.")

    while True:
        guess = input("Enter your guess: ").lower()

        if guess == "exit":
            print("Game ended")
            exit()

        if not guess.isdigit():
            print("Please enter a valid number or 'exit'")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100")
            continue

        if guess == number:
            print("Correct! You guessed it in", attempts, "attempts")
            break

        elif guess < number:
            print("Too low")

        else:
            print("Too high")

    
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break 

        elif again in ["no", "n"]:
            print("Game ended")
            exit()  

        else:
            print("Invalid input, please enter yes or no")