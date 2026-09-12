# methods are functions that belong to the objects


class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello", self.name)


s1 = Student("Bhupendra")

s1.hello()
