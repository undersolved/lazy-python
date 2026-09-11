f = open("15_read-io/test.txt", "r")

line1 = f.readline()

print(line1)

# reads the first line

f.close()

"""
'r' = read - default mode
'w' = write mode - overwrites the file
'a' = append - adds at the end
'x' = exclusive file creation opening
"""
