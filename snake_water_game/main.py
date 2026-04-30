import random

print("Snake Water Gun Game Started")
print("Type 'exit' anytime to quit\n")

choices = ["snake", "water", "gun"]

user_score = 0
computer_score = 0
games_played = 0

start = input("Do you want to play Snake Water Gun? (yes/no): ").lower()

if start in ["no", "n"]:
    print("Game ended")
    exit()

while True:

    computer = random.choice(choices)

    user = input("\nEnter snake/water/gun: ").lower()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid choice, try again")
        continue

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie")

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):

        print("You win this round")
        user_score += 10

    else:
        print("Computer wins this round")
        computer_score += 10

    games_played += 1

  
    while True:
        again = input("\nDo you want to play again? (yes/no or exit): ").lower()

        if again in ["yes", "y"]:
            break   # new round start

        elif again in ["no", "n", "exit"]:
            print("Game ended")
            games_played += 0
            user = "exit"
            break

        else:
            print("Invalid input, please type yes or no")

    if user == "exit" or again in ["no", "n", "exit"]:
        break

print("\n--- GAME OVER ---")
print("Total Games Played:", games_played)
total_possible_score = games_played * 10

print("Your Score:", user_score, "out of", total_possible_score)
print("Computer Score:", computer_score, "out of", total_possible_score)

if user_score > computer_score:
    print("Final Winner: You Win the Game")

elif computer_score > user_score:
    print("Final Winner: Computer Wins the Game")

else:
    print("Final Result: Draw")