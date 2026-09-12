class Numbers:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Numbers(self.values + other.values)


n1 = Numbers(1)
n2 = Numbers(2)
result = n1 + n2
print(result.values)
