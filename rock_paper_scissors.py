import random

def game():
    options = ["rock", "paper", "scissors"]
    print("Type 'rock', 'paper', or 'scissors'. Type 'quit' to exit.")
    
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("End")
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        print("Computer chose: ", "computer_choice")

        
        if user_choice == computer_choice:
            print("Tie")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win")
        else:
            print("You lose")

game()