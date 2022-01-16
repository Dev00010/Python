f1=open("C:\\Users\\Dev\\Documents\\abc.txt","r")
upper=0
lower=0
while True:
    c=f1.read(1)
    if c.isupper():
        upper=upper+1
    if c.islower():
        lower=lower+1
    if not c:
        break
print("Upper=>",upper)
print("Lower=>",lower)
f1.close()