import random

num=random.randint(1,10)
for i in range(4):
  try:
    guess= int(input("Enter your guess number between 1 to 10: \n")) 
    if guess==num:
      print("You won")
      break
    elif guess>num:
      print("Your guess is greater")
    else:
      print("Your guess is smaller")
  except ValueError:
     print("Enter a valid number.")
print("Guess limit is over! Tray Again.")
 
   