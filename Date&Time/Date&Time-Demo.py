import time
current = time.localtime(time.time())
print("Year:", current.tm_year)
print("Month:", current.tm_mon)
print("Date:", current.tm_mday)
print("Weekday:", current.tm_wday)
print("Day:", end=' ')
if current.tm_wday == 0:
    print("Monday")
elif current.tm_wday == 2:
    print("Tuesday")
elif current.tm_wday == 3:
    print("Wednesday")
elif current.tm_wday == 4:
    print("Thursday")
elif current.tm_wday == 5:
    print("Friday")
elif current.tm_wday == 6:
    print("Saturday")
else:
    print("Sunday")
print("Yearday:", current.tm_yday)
print("Hour:", current.tm_hour)
print("Minutes:", current.tm_min)
print("Seconds:", current.tm_sec)