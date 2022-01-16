n=int(input("Enter Number=>"))
i=n
f=1
while i>=1:
    if i==1:
        print(i,end='')
    else:
        print(i,"*",end='')
    f = f * i
    i=i-1

print("\nFactorial=>",f)