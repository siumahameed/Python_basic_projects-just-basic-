operator = input("Enter the operator you want to use(+,-,*,/): ")

num1=int(input("Enter the first number: ")) 
num2=int(input("Enter the second number: "))

if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)
else:
    print("Invalid operator")