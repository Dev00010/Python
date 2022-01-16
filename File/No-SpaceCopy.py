f1=open("C:\\Users\\Dev\\Documents\\abc.txt","r")
f2=open("C:\\Users\\Dev\\Documents\\nospace.txt","w")
while True:
    c=f1.read(1)
    if not c:
        break
    if not c == ' ':
      f2.write(c)
f1.close()
f2.close()

print("Copied")