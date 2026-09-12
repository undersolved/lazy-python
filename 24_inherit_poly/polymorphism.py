# one method multiple forms

print(len("Bhupendra"))
print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(len({"a": 1, "b": 2}))


class Bird:
    def makeSound(self):
        print("bhakkkkkkk")


class Cat:
    def makeSound(self):
        print("meowwww")


for animal in [Bird(), Cat()]:
    animal.makeSound()
