import random

print("Math Challenge Game Started")
print("Type 'exit' to quit\n")

user_score = 0
rounds = 0
wrong_streak = 0

while True:

    a = random.randint(1, 20)
    b = random.randint(1, 20)

    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        correct_answer = a + b
    elif operator == "-":
        correct_answer = a - b
    else:
        correct_answer = a * b

    user = input(f"What is {a} {operator} {b}?: ").lower()

    if user == "exit":
        break

    if not user.lstrip("-").isdigit():
        print("Invalid input")
        continue

    user = int(user)

    if user == correct_answer:
        print("Correct!")
        user_score += 10
        wrong_streak = 0

    else:
        print("Wrong! Correct answer was:", correct_answer)
        wrong_streak += 1

        print("Wrong streak:", wrong_streak, "/ 3")

        if wrong_streak == 3:
            print("\nYou gave 3 wrong answers continuously!")
            print("Game Over")
            break

    rounds += 1

print("\n--- GAME OVER ---")
print("Rounds Played:", rounds)
print("Your Score:", user_score, "out of", rounds * 10)