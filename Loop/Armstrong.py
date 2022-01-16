n=int(input("Enter Number=>"))
tmp=n
s=0
while n>0:
    x=n%10
    s=s+(x*x*x)
    n=n//10
print("Number=>",s)
if s==tmp:
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")