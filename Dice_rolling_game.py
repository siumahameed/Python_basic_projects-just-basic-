
import random

name = input("Enter your name: ")
print(f"Hello {name}, Welcome to the game")
while True:
  choice= input("Do you want to play? (y/n)")

  if choice == "y" or choice =="Y":
      dice1= random.randint(1,6)
      dice2= random.randint(1,6)
      print(f"You got ({dice1},{dice2})")
  elif choice == "n" or choice == "N":
     print(f"Thank You {name} for coming. Have a nice day.")
     break
  else:
    print("Invalid Input")


    