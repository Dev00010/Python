import os

path="c:\\"

dir_list = os.listdir(path)

for x in dir_list:

    x="c:\\" +x
    print(x," -- ",os.path.isfile(x)," -- ",os.path.isdir(x))
