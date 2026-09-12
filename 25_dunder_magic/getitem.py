class myList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]


m1 = myList([1, 2, 3, 4, 5])
print(m1[2])
