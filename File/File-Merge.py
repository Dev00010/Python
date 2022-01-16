f1=open("C:\\Users\\Dev\\Documents\\india1.txt","w")
f2=open("C:\\Users\\Dev\\Documents\\russia.txt","r")
f3=open("C:\\Users\\Dev\\Documents\\usa.txt","r")
while True:
    r=f2.read(1)
    if not r:
        break
    f1.write(r)
while True:
    u=f3.read(1)
    if not u:
        break
    f1.write(u)
f1.close()
f2.close()
f3.close()

print("Copied")