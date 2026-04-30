import random
import requests

print("Hangman Game Started")
print("Type 'exit' anytime to quit\n")


def get_random_word():
    try:
        url = "https://random-word-api.herokuapp.com/word"
        response = requests.get(url)
        return response.json()[0]
    except:
        return random.choice(["python", "computer", "banana", "flower"])


def get_hint(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()

        meanings = data[0]["meanings"][0]["definitions"]
        hints = [m["definition"] for m in meanings]

        return hints

    except:
        return [f"This word has {len(word)} letters"]


total_score = 0
total_games = 0

win_streak = 0
loss_streak = 0

while True:

    word = get_random_word()
    hint_list = get_hint(word)

    guessed_letters = []
    attempts = 6
    hint_used = 0

    print("\nNew Game Started!")

    while attempts > 0:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Attempts left:", attempts)
        print("Hints left:", 2 - hint_used)

        guess = input("Enter letter / hint: ").lower()

        if guess == "exit":
            print("\nGame Ended")
            print("Total Games:", total_games)
            print("Total Score:", total_score)
            exit()

        # hint system
        if guess == "hint":
            if hint_used < 2:
                print("HINT:", hint_list[hint_used % len(hint_list)])
                hint_used += 1
            else:
                print("No hints left!")
            continue

        # validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print("Already guessed")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nYou won! Word was:", word)

            total_score += 20
            win_streak += 1
            loss_streak = 0

            # 🔥 BONUS RULE
            if win_streak == 3:
                print("🔥 BONUS! 3 WIN STREAK +20 POINTS")
                total_score += 20
                win_streak = 0

            break

    else:
        print("\nYou lost! Word was:", word)

        loss_streak += 1
        win_streak = 0

        # 💀 OUT RULE
        if loss_streak == 3:
            print("\n💀 OUT! 3 consecutive losses")
            print("Game Over Automatically")
            print("Total Games:", total_games)
            print("Total Score:", total_score)
            exit()

    total_games += 1

    # summary
    print("\n--- ROUND SUMMARY ---")
    print("Total Games:", total_games)
    print("Total Score:", total_score)

    # play again system
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again in ["yes", "y"]:
            break

        elif again in ["no", "n"]:
            print("\n--- FINAL RESULT ---")
            print("Total Games Played:", total_games)
            print("Total Score:", total_score)
            exit()

        elif again == "exit":
            print("\nGame Exited")
            print("Total Games:", total_games)
            print("Total Score:", total_score)
            exit()

        else:
            print("Invalid input, please type yes or no")

