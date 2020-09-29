from random import randint

items = ["Rock", "Scissors", "Papper"]

computer = items[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Scissors, Papper: ")
    if player == computer:
        print("Tie!!")
    elif player == "Rock":
        if computer == "Papper":
            print("You lose", computer, "covers", player)
        else:
            print("You win", player,"smashes",computer)
    elif player == "Papper":
        if computer == " Scissors":
            print("You lose", computer ,"Cuts",player)
        else:
            print("Yo win", player,"covers",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer,"smashes",player)
        else:
            print("You win", player, "cuts",computer)
    else:
        print("Check your spelling!!!")

player = False

computer = items[randint(0, 2)]