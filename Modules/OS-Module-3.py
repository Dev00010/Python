import os

cwd = os.getcwd()
print("Current working directory:", cwd)

path="c:\\"
dir_list = os.listdir(path)

print("Files and directories '", dir_list)

for x in dir_list:
    print(x)
