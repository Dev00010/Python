set1={11,55,66,77,45,78}
set2={11,66,77 }
set3={1,2,3,4}
set4={22,66,77,7,45,9}
print("SUPERSET ::")
print(set1.issuperset(set2))
print(set1.issuperset(set3))
print(set1.issuperset(set4))
print("SUBSET ::")
print(set1.issubset(set2))
print(set1.issubset(set3))
print(set1.issubset(set4))
