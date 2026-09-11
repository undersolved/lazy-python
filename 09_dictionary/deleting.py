# using del to delete

student = {"name": "Bhupendra Singh", "age": 20, "isStudent": True}

del student["age"]

print(student)

# using .pop

student = {"name": "Bhupendra Singh", "age": 20, "isStudent": True}

student.pop("age")
print(student)

# using .clear -- full blank
