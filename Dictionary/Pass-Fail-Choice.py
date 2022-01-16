marks={1:33,2:56,3:95,4:12,5:65}
print("Enter 1 to print pass students")
print("Enter 2 to print fail students")
x=int(input("Enter your choice=>"))

if x==1:
    print("Rollno \t Marks \t Pass/Fail")
    for key, value in marks.items():
        if value > 50:
            print(key, "   \t", value, "\t Pass")
else:
    print("Rollno \t Marks \t Pass/Fail")
    for key,value in marks.items():
        if value < 50:
            print(key, "   \t", value, "\t Fail")