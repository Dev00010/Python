num1=int(input("Enter Number 1=>"))
num2=int(input("Enter Number 2=>"))
print("Enter + for Addition")
print("Enter - for Subtraction")
print("Enter / for Division")
print("Enter * for Multiplication")
choice=(input("Enter your choice=>"))
if choice=="+":
    print("Addition=>",num1+num2)
elif choice=="-":
    print("Subtraction=>",num1-num2)
elif choice=="/":
    print("Divison=>",num1/num2)
else:
    print("Multiplication=>",num1*num2)