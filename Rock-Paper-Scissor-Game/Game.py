import random

print("       WELCOME TO THE GAME       ")
print("  GAME NAME: ROCK PAPER SCISSOR  ")
print('         WINNING RULES:\n'
      "RULE1: Rock vs Paper -> Paper wins \n"
      "RULE2: Rock vs Scissors -> Rock wins \n"
      "RULE3: Paper vs Scissors -> Scissor wins \n")

while True:
    user_choice = input("Enter your choice:\nrock\npaper\nscissor").lower()
    print(f"User choice is: {user_choice}")

    Computer_choice = random.choice(["rock", "paper", "scissor"])
    print(f"Computer choice is: {Computer_choice}")

    if user_choice == Computer_choice:
        print("It's a draw!")
    elif(user_choice == "rock" and Computer_choice == "scissor"):
        print("YOU WONN!")

    elif (user_choice == "paper" and Computer_choice == "rock"):
        print("YOU WONN!")

    elif(user_choice == "scissors" and Computer_choice == "paper"):
        print(" YOU WONN!")
  
    elif(user_choice == "scissor" and Computer_choice == "rock"):
        print("YOU LOSE!")

    elif (user_choice == "rock" and Computer_choice == "paper"):
        print("YOU LOSE!")

    elif(user_choice == "paper" and Computer_choice == "scissor"):
        print("YOU LOSE!")

    else:
        print("Invalid Choice")

    play_again = input("Do you want to play again? (Y/N)").lower()
    if play_again != "y":
        break    


print("Thank you for playing!")
