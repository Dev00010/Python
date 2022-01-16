# Append can be used in this, as tuple converted to list in line 3
tupleD=(11,22,33,44,55)
list1=list(tupleD)
list1.append(101)
tupleD =tuple(list1)
print(tupleD)