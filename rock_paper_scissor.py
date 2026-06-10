"""
WORKFLOW OF PROJECT
1. Importing the libraries
2. Taking the input from the user(rock, paper, scissor)
3. COMPUTER choice (computer will chocess randomaly not conditionally)
4. Comparing the user input and computer input
5. Displaying the result

case:1
A= rock
rock vs rock = tie
rock vs paper = paper wins
rock vs scissor = rock wins




case:2
B= paper
paper vs rock = paper wins
paper vs paper = tie
paper vs scissor = scissor wins



case:3
C= scissor
scissor vs rock = rock wins
scissor vs paper = scissor wins
scissor vs scissor = tie


"""

import random
print("\033[1;32mWelcome to the Rock, Paper, Scissor Game!\033[0m")
items_list = ["rock", "paper", "scissor"]
user_choice = input("\033[1;34mEnter your choice (rock, paper, scissor): \033[0m").lower()
computer_choice = random.choice(items_list)
print(f"\033[1;35mUser chose: {user_choice}\033[0m")
print(f"\033[1;35mComputer chose: {computer_choice}\033[0m")

if user_choice == computer_choice:
    print("\033[1;31mboth choice are same, it's a tie\033[0m")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("\033[1;31m paper covers rock, computer wins\033[0m")
    else:
        print("\033[1;32m rock smashes scissor, user wins\033[0m") 
elif user_choice == "paper":
    if computer_choice == "rock":
        print("\033[1;32mpaper covers rock, user wins\033[0m")
    else:
        print("\033[1;31mscissor cuts paper, computer wins\033[0m")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("\033[1;31mrock smashes scissor, computer wins\033[0m")
    else:
        print("\033[1;32mscissor cuts paper, user wins\033[0m")
else:
    print("\033[1;31minvalid input, please choose rock, paper, or scissor\033[0m")   
                       



