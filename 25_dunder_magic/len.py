class Basket:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


b = Basket([1, 2, 3, 4, 5, 6])
print(len(b))
