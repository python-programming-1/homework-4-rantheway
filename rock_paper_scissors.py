from random import randint

t = ["r", "p", "s"]
computer = t[randint(0,2)]

computer_score = 0
player_score = 0

player = False

while player == False:

    player = input("make a move! (r/s/p):")
    if player == computer:
        print("Draw!")
    elif player == "r":
        if computer == "p":
            print("You chose rock and the computer chose paper. You lose!")
            computer_score += 1
        else:
            print("You chose rock and the computer chose scissors. You win!")
            player_score += 1
    elif player == "p":
        if computer == "s":
            print("You chose paper and the computer chose scissors. You lose!")
            computer_score += 1
        else:
            print("You chose paper and the computer chose rock. You win!")
            player_score += 1
    elif player == "s":
        if computer == "r":
            print("You chose scissors and the computer chose rock. You lose!")
            computer_score += 1
        else:
            print("You chose scissors and the computer chose paper. You win!")
            player_score += 1
    elif player == "sc":
        print("human:", player_score, ", computer:", computer_score)
    else:
        print("That's not a valid play. Check your spelling!")
   
    print("Do you want to play again? (Y/N)") 
    ans = input() 
    if ans == 'n' or ans == 'N': 
        break
    else: 
        player= False
        computer = t[randint(0,2)]
print("Thanks bye!") 
    