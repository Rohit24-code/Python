import sys
import random


print('')
playersChoice = input("Enter...\n 1 for Rock \n 2 for paper \n 3 for scissors : \n \n")

player =int(playersChoice)

if player < 1 | player>3:
    sys.exit("you must enter 1,2,or 3.")

# it will come one from given string 
computerChoice = random.choice("123")


computer = int(computerChoice)

print("")
print("you chose " + playersChoice + ".")
print("Python choose" + computerChoice + ".")
print("")

if player == 1:
    print("You win !")
elif player==2 and computer ==1:
    print('You win:')
elif player == 3 and computer ==2 :
    print("you win!")
elif player == computer :
    print("its a tie")
else : print("python wins!")




