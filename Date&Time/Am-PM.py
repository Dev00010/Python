import time
current = time.localtime(time.time())
print("Hour:", current.tm_hour)
if current.tm_hour>=0 and current.tm_hour<12:
    print("!!!AM!!!")
else:
    print("!!!PM!!!")