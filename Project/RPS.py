from random import randint # choices[randint(len(choices))]
 
# # # RPS
choices = ("Rock", "Paper", "Scissors")
 
 
def winner(pc, cc):  # check who wins. rock > scissors > paper > rock
    if pc == cc:
        print("Draw")
    elif pc == "Rock":
        if cc == "Paper":
            print("Computer Wins")
        else:
            print("Player Wins")
    elif pc == "Paper":
        if cc == "Scissors":
            print("Computer Wins")
        else:
            print("Player Wins")
    elif pc == "Scissors":
        if cc == "Rock":
            print("Computer Wins")
        else:
            print("Player Wins")
    else:
        print("Error")
 
 
while True:  # Loop
    playersChoice = input("\nRock, Paper or Scissors? (E to Exit)\n") # Players input
    playersChoice = playersChoice.capitalize()
 
    if playersChoice in choices:
 
        computersChoice = choices[randint(0, len(choices) - 1)]  # computer choice is random of the three
        print("Computer Plays: " + computersChoice)
 
        winner(playersChoice, computersChoice)
    elif playersChoice == "E" or playersChoice == "Exit":
        break
    else:
        print("Invalid Move")