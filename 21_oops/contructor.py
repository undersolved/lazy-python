# constructor is an init function or initialise function __init__()
# python automatically invokes constructor if you don't use init function


class Person:
    def __init__(self, name, age):
        self.fullName = name
        self.age = age
        print("person created")

    def display(self):
        print(f"Name is : {self.fullName} and Age is : {self.age}")


p1 = Person("Bhupendra", 25)

p1.display()

print(p1.fullName)
