import random

print("Rock Paper Scissors Game Started")
print("Type 'exit' to quit\n")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
games_played = 0

start = input("Do you want to play? (yes/no): ").lower()

if start in ["no", "n"]:
    print("Game ended")
    exit()

while True:

    user = input("\nEnter rock/paper/scissors: ").lower()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)



    if user == computer:
        print("Draw")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win")
        user_score += 10

    else:
        print("Computer wins")
        computer_score += 10

    games_played += 1

    again = input("\nPlay again? (yes/no): ").lower()

    if again in ["no", "n"]:
        break

    elif again not in ["yes", "y"]:
        print("Invalid input, exiting")
        break


print("\n--- GAME OVER ---")
print("Games Played:", games_played)
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Winner: You")

elif computer_score > user_score:
    print("Winner: Computer")

else:
    print("Result: Draw")