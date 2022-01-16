salary=int(input("Enter Salary=>"))
da=salary*0.52
ma=salary*0.10
hra=salary*0.10
va=salary*0.10
ltc=salary*0.05
GrossSalary=salary+da+ma+hra+va+ltc
Netsalary=GrossSalary-1000
print("Final Salary=>",Netsalary)