import os
path="A:\\Trojan-Python"
os.chdir(path)
cwd=os.getcwd()
print("CWD=>",cwd)
list=os.listdir()

for x in list:
    x="A:\\Trojan-Python\\" +x
    print(x)
    if ".txt" in x:
        path = "A:\\Trojan-Python\\New"
        os.chdir(path)

    else:
        print("Not TXT")
