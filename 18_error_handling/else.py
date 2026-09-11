try:
    a = int(input("enter a number"))
except ValueError:
    print("invalid input")
else:
    print("Your age is :", a)

# else runs if try is successfull
# finally runs everytime - like in file not found error
