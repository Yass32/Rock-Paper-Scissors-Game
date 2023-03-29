import random as random

CHOICES = {0 : "Rock", 1 :"Paper", 2 :"Scissors"}

RESULTS = {
    (0,0) : "Tie!",
    (0,1) : "Computer Wins!",
    (0,2) : "User Wins!",
    (1,0) : "User Wins!",
    (1,1) : "Tie!",
    (1,2) : "Computer Wins!",
    (2,0) : "Computer Wins!",
    (2,1) : "User Wins!",
    (2,2) : "Tie!"
}

def game(a, b):
    print(RESULTS[(a,b)])

print("Welcome to Rock, Paper, Scissors game")
answer = input("Are you ready to play, yes or no \n")
if answer.lower() == "yes":
    rounds = int(input("How many rounds would you like to play \n")) 
    for i in range(rounds):
        user_choice = int(input("Choose:\n 0 for Rock \n 1 for Paper \n 2 for Scissors \n"))
        if user_choice in CHOICES:
            print(f"User chose {CHOICES[user_choice]}")
            computer_choice = random.randint(0,2)
            print(f"Computer chose {CHOICES[computer_choice]}")
            game(user_choice, computer_choice)
        else:
            print("Error, you didn't choose a number between 0 and 2")
            break
else:
    print("Game Over")
