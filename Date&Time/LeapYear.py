import time
current = time.localtime(time.time())
print("Year:", current.tm_year)
if current.tm_year%4==0:
    if current.tm_year%100==0:
        if current.tm_year%400==0:
            print("Leap Year")
        else:
            print("Not A Leap Year")
    else:
        print("Leap Year")
else:
    print("Not A Leap Year")