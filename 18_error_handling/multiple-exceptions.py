try:
    a = int(input("enter a number"))
    b = 10 / a
    print("result :", b)
except (ValueError, ZeroDivisionError):
    print("invalid input")
