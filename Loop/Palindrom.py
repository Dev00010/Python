n = int(input("Enter Number=>"))
cno = n
s = 0
print("Number=>", n)

while n > 0:
    x = n % 10
    s = s * 10 + x
    n = n // 10


print("Reverse Number=>", s)
if s == cno:
    print("It's a palindrome number")
else:
    print("It's not a palindrome number")
