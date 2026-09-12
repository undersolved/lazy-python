class Parent:
    def speak(self):
        print("speaking for parent class")


class Child(Parent):
    pass


# c = Child()
# c.speak()

###################################################################################


class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("dog barks")


class Cat(Animal):
    def speak(self):
        print("cat meows")


d = Dog()
c = Cat()

print(d.speak(), c.speak())
