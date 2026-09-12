num = [10, 20, 30]

it = iter(num)

# print(next(it))
# print(next(it))
# print(next(it))

# reading files one by one line - controls memory consumption

# now let's make a custom iterator


class customIterator:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


for i in customIterator(5):
    print(i)
