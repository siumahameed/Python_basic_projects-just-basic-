name = input("Enter your name: ")
print(f"Hello {name}, Welcome to PYTHON RESTAURANT")

menu={
    "Pizza": 300,
    "Burger": 120,
    "Pasta": 150,
    "Salad": 150,
    "Meatbox": 180,
    "Coffee":100,
    "Tea": 30
}
print("Our food menu is:")
print("Pizza=300TK \nBurger=120TK \nPasta=150TK \nSalad=150TK \nMeatbox=180TK \nCoffee=100TK \nTea=30TK")

Total_bill = 0
while True:
  order1= input("What do you want to order:\n")
  if order1 in menu:
     Total_bill+= menu[order1]
     print(f"You have ordered {order1} and your bill is: {Total_bill}Taka")
     ask= input("Do you want to order something else? (y/n): ").lower()
     if ask=="y":
         order2= input("What do you want to order:\n")
         if order2 in menu:
             Total_bill+=menu[order2]
             print(f"You have ordered {order1} and {order2}, your bill is: {Total_bill}Taka")
         else:
             print("Sorry! Your ordered item is not available yet.")
     elif ask=="n":
          print(f"Thank you! Enjoy your food")   
     else:
        print("Sorry! Your ordered item is not available yet.")
     break
  else:
     print("Sorry! Your ordered item is not available yet.")
     
     
     
"""
menu = {
    'pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to Python Restaurant")
print("pizza: 60 Rs\nPasta: 40 Rs\nBurger: 60 Rs\nsalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")

"""

"""

menu = {
"pizza":120,
"burger": 30,
"coffee":10,
"chowmein":30,
"maggie":40,
"dosa": 60,
}

a = input("Hello, sir\nWhat Help do you want?\n")

def order():
    total_order = 0
    if a == "order":
        b = input("What would you like to order?\n")
        if b in menu:
            total_order += menu[b]
            print(f"{b} has been added to your list")
        else:
            print("We dont have that item sir")
            
        
        c = input("Want Anything else?\n")
        
        if c == 'yes':
            d = input("What do you want?\n")
            if d in menu:
                total_order += menu[d]
                print(f"{d} has been added to your list")
                print(f"your Total bill is {total_order}")
            else:
                print("We dont have that sir")
        elif c == 'no':
            print(f"Your total bill is {total_order}")       
            
        if total_order == 0:
            print("Must buy something whenever you visit next time")
    elif a == "list":
        print("___ARISE RESTU MENU___")
        print("1. pizza - 120₹\n2. burger - 30₹\n3. coffee - 10₹\n3. chowmein - 30₹\n4. maggie - 40₹\n5. dosa - 60₹")                 
        
order()

"""