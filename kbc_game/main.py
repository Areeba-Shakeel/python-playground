quiz1 = ["What is the capital of Pakistan?"]
options1 = ["a) Karachi", "b) Islamabad", "c) Multan", "d) Lahore"]
answer1 = "b"

quiz2 = ["What is the national sport of Pakistan?"]
options2 = ["a) Cricket", "b) Hockey", "c) Football", "d) Squash"]
answer2 = "b"   

quiz3 = ["Who was the founder of Pakistan?"]
options3 = ["a) Allama Iqbal", "b) Liaquat Ali Khan", "c) Muhammad Ali Jinnah", "d) Fatima Jinnah"]
answer3 = "c"

quiz4 = ["Which river is known as the 'Lifeline of Pakistan'?"]
options4 = ["a) Indus River", "b) Jhelum River", "c) Chenab River", "d) Ravi River"]
answer4 = "a"   

quiz5 = ["What is the national flower of Pakistan?"]
options5 = ["a) Rose", "b) Jasmine", "c) Lily", "d) Tulip"]
answer5 = "b"

a = input("Do you want to play the quiz game? (yes/no): ")
      
      
if a.lower() in ["yes", "y"]:
    reward = 0 

    print(quiz1[0])
    for option in options1:
        print(option)
    answer1 = input("Enter your answer (a/b/c/d): ")
    if answer1.lower() == "b":
        reward += 10000
    else:
        print("Wrong answer, better luck next time!")
        print(f"You earned {reward} Rs.")
        exit()

    print(quiz2[0])
    for option in options2:
        print(option)
    answer2 = input("Enter your answer (a/b/c/d): ")            
    if answer2.lower() == "b":
        reward += 10000
    else:
        print("Wrong answer, better luck next time!")
        print(f"You earned {reward} Rs.")
        exit()


    print(quiz3[0])
    for option in options3:
        print(option)
    answer3 = input("Enter your answer (a/b/c/d): ")            
    if answer3.lower() == "c":
        reward += 10000
    else:
        print("Wrong answer, better luck next time!")
        print(f"You earned {reward} Rs.")
        exit()

    print(quiz4[0])
    for option in options4:
        print(option)
    answer4 = input("Enter your answer (a/b/c/d): ")            
    if answer4.lower() == "a":
        reward += 10000
    else:
        print("Wrong answer, better luck next time!")
        print(f"You earned {reward} Rs.")
        exit()

    print(quiz5[0])
    for option in options5:             
        print(option)
    answer5 = input("Enter your answer (a/b/c/d): ")            
    if answer5.lower() == "b":
        reward += 10000
    else:
        print("Wrong answer, better luck next time!")
        print(f"You earned {reward} Rs.")
        exit()


    if reward == 50000:
        print("Congratulations! You won the quiz game and earned 50,000 Rs!")
    else:
        print(f"You earned {reward} points. Better luck next time!")


else:   
    print("Maybe next time!")