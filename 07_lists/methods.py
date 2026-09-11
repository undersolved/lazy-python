fruits = ["apple", "banana", "mango", "cherrry", "watermelon"]

num = [10, 20, 30, 40, 50]

num.append(50)
print(num)

num.extend([77])

print(num)

num.remove(10)
print(num)

num.pop(2)
print(num)


num.insert(2, 199)
print(num)

num = num + [500, 600, 800]
print(num)

num.sort(reverse=True)
print(num)
