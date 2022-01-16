try:
    a = int(input("Enter Number=>"))
    b = int(input("Enter Number=>"))
    ans = a / b
    print(ans)
except ZeroDivisionError:
    print("Why 0????")
except ValueError:
    print("Why Character??")
except:
    print("Other Error")