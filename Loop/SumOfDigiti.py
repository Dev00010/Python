n = int(input("Enter Number=>"))
cno = n
s = 0
print("Number=>", n)

while n > 0:
    x = n % 10
    s = s + x
    n = n // 10


print("Sum of Digit=>", s)
