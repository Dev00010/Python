list = [1,-5,3,-10,7]
p=0
n=0
for x in list:
    if x>0:
        p=p+1
        print("Positive Number")
    else:
        print("Negative Number")
        n=n+1
print("Total Positive Number=>",p)
print("Total Negative Number=>",n)
