# generator uses yeild to return each value one by one


def count_upto(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_upto(5):
    print(num)
