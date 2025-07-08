#ask the user to make a choice
#If choice is not valid 
#  print "Invalid input"
# if choice is valid
# let the computer make a choises
# show the choices with emoji
# declare the winner
# ask if they want to play again
# terminate the prog with the greet.
import random

while True:
 guess= input("Chosse one Rock, Paper or Scissors(r/p/s): ").lower()
 choice=("r","p","s")
 if guess in choice:
    com =random.choice(choice)
    print(f"Computer chose {com}")
    print(f"You chose {guess}")
    if guess == com:
        print("Tie") 
    elif guess=="p" and com=="s":
        print("You lose")
    elif guess=="s" and com=="p":
        print("You Win")
    elif guess=="r" and com=="p":
        print("You lose")
    elif guess=="p" and com=="r":
        print("You win")
    elif guess=="r" and com=="s":
        print("You win")
    elif guess=="r" and com=="s":
        print("You Lose")
    ask=input("Continue? (y/n): ").lower()
    if ask=="n":
      print("Thanks for playing")
      break
 else:
    print("Invalid Choice")

