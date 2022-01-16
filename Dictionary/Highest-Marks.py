marks={1:33,2:56,3:95,4:12,5:65}
print("Rollno \t Marks \t Pass/Fail")
x=list(marks.values())
y=list(marks.keys())
m=max(x)
for key,value in marks.items():

    if m==value:
        print(key,"   \t",value,"   \t")