nums = [1, 2, 3, 4, 5]

# jo kaam loop se hota hai

product = 1

for num in nums:
    product = product * num
print(product)

# same kaam reduce se karten hain

from functools import reduce

productive = reduce(lambda x, y: x * y, nums)
print(productive)
