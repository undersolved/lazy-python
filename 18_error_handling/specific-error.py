try:
    a = int(input("enter a number"))
    b = 10 / a
    print("result :", b)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("you have divided by zer")
