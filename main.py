from random import randint

t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#assign a random play to the computer
computer = t[randint(0,4)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors, Lizard, or Spock?: ")
    if player == computer:
        print("Tie!")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer =="Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)    
    
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        elif computer == "Rock":
            print("You win!", player, "covers", computer)
        elif computer == "Lizard":
            print("You lose!", computer, "eats", player)
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
        elif computer == "Paper":
            print("You win!", player, "cuts", computer)
        elif computer == "Lizard":
            print("You win!", player, "decapitates", computer)
        elif computer == "Spock":
            print("You lose!", computer, "smashes", player)

    elif player == "Lizard":
        if computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer == "Paper":
            print("You win!", player, "eats", computer)
        elif computer == "Scissors":
            print("You lose!", computer, "decapitates", player)
        elif computer == "Spock":
            print("You win!", player, "poisons", computer)

    elif player == "Spock":
        if computer == "Rock":
            print("You win!", player, "vaporizes", computer)
        elif computer == "Paper":
            print("You lose!", computer, "disproves", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You lose!", computer, "poisons", player)
    else:
        print("That's an illogical move, please try again!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,4)]
