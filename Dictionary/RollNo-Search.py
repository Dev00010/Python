marks={1:33,2:56,3:95,4:12,5:65}
t=0
x=int(input("Enter Roll number to search=>"))
y=list(marks.keys())
z=list(marks.values())
for key,value in marks.items():
    if key == x:
        print("Rollno \t Marks ")
        print(key, "   \t", value)
        t=1
if t==0:
    print("!!!No Record Found!!!")