n=int(input("Enter Limit=>"))
f=1
for i in range(1,n+1):
    print(i,"*",end=' ')
    f=f*i

print("Factorial=>",f)