#Assessed Task 2 - Week 3
from random import randint

playerChoice = int(input("From the list below, enter the number of the object you are selecting and press ENTER \n 1 = Rock \n 2 = Paper \n 3 = Scissors \n"))

computerChoice = randint(1, 3)

def game(choice):
    if choice == 1:
        playerChoosesRock(choice)
    elif choice == 2:
        playerChoosesPaper(choice)
    elif choice == 3:
        playerChoosesScissors(choice)
    else:
        print("Invalid Input")

def playerChoosesRock(choice):
    if choice == 1 and computerChoice == 1:
        print("Computer selects:", computerChoice)
        print("Draw")
    elif choice == 1 and computerChoice == 2:
        print("Computer selects:", computerChoice)
        print("You lost!")
    
    elif choice == 1 and computerChoice == 3:
        print("Computer selects:", computerChoice)
        print("You won!")
        
def playerChoosesPaper(choice):
    if choice == 2 and computerChoice == 1:
        print("Computer selects:", computerChoice)
        print("You won!")
        
    elif choice == 2 and computerChoice == 2:
        print("Computer selects:", computerChoice)
        print("Draw")
    
    elif choice == 2 and computerChoice == 3:
        print("Computer selects:", computerChoice)
        print("You lost!")
        
def playerChoosesScissors(choice):
    if choice == 3 and computerChoice == 1:
        print("Computer selects:", computerChoice)
        print("You lost!")
        
    elif choice == 3 and computerChoice == 2:
        print("Computer selects:", computerChoice)
        print("You won!")
    
    elif choice == 3 and computerChoice == 3:
        print("Computer selects:", computerChoice)
        print("Draw")
        
game(playerChoice)