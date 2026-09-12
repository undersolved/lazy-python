class Car:
    carCompany = "TATA"

    def __init__(self, model, color):
        self.model = model
        self.color = color
        print("Car created")


s1 = Car("Nexon", "Red")
print(s1.model, s1.color)

s2 = Car("Safari", "Black")
print(s2.model, s2.color)
