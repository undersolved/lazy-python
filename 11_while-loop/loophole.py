# break and continue

i = 1

while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("loop ended")

m = 0

while m < 5:
    if m == 2:
        m += 1
        continue
    print(m)
    m += 1
print("loop has ended")
