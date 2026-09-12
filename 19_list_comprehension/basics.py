# its a shortcut used to create a list by using loop

# without LC

num = [1, 2, 3, 4, 5]
square = []

for n in num:
    square.append(n**2)


# with LC

num2 = [10,20,30,40,59]

square2 = [n**2 for n in num2 if n%2==1]

numz = [n for n in range(15) if n%2==0]

print(numz)