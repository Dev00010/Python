n=int(input("Enter Number=>"))
x=0
for i in range(2,n):
    if n%i==0:
        x=1
        break
if x==0:
    print("It is a prime number")
else:
    print("It is not a prime number")