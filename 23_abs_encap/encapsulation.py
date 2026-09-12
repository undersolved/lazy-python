"""
Wrapping data and functions into a single object
"""


class bankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # so this is a private attribute - therefore this is not accessible to the outer scope

    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance


acc = bankAccount("Bhupendra", 1800)
print(acc.getBalance())

acc.deposit(500)
print(acc.getBalance())

# print(acc.__balance)
