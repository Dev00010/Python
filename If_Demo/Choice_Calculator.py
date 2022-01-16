num1=int(input("Enter Number 1=>"))
num2=int(input("Enter Number 2=>"))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Division")
print("Enter 4 for Multiplication")
num3=int(input("Enter your choice=>"))
if num3==1:
    print("Addition=>",num1+num2)
elif num3==2:
    print("Subtraction=>",num1-num2)
elif num3==3:
    print("Divison=>",num1/num2)
else:
    print("Multiplication=>",num1*num2)