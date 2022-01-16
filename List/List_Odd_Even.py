list=[1,2,3,4,5,6]
se=0
ce=0
so=0
co=0
for x in list:
    if x%2==0:
        se=se+x
        ce=ce+1
    else:
        so=so+x
        co=co+1
print("Even Number:: Sum=>",se," Count=>",ce)
print("Odd Number:: Sum=>",so," Count=>",co)