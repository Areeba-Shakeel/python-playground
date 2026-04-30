import random

print("Dice Game Started")
print("Type 'exit' to quit\n")

user_score = 0
computer_score = 0
rounds = 0

while True:

    user = input("Press Enter to roll dice (or type exit): ").lower()

    if user == "exit":
        break

    # 🔥 FIX: invalid input check
    if user != "":
        print("Invalid input, press Enter or type 'exit'")
        continue

    user_dice = random.randint(1, 6)
    computer_dice = random.randint(1, 6)

    print("You rolled:", user_dice)
    print("Computer rolled:", computer_dice)

    if user_dice > computer_dice:
        print("You win this round")
        user_score += 10

    elif user_dice < computer_dice:
        print("Computer wins this round")
        computer_score += 10

    else:
        print("Draw")

    rounds += 1

    while True:
        again = input("\nPlay again? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break

        elif again in ["no", "n"]:
            user = "exit"
            break

        else:
            print("Invalid input, please type yes or no")

    if user == "exit":
        break

# FINAL RESULT
print("\n--- GAME OVER ---")
print("Rounds Played:", rounds)
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Final Winner: You")

elif computer_score > user_score:
    print("Final Winner: Computer")

else:
    print("Result: Draw")