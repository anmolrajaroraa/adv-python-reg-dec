# class Student:
#     id = 101
#     name = 'Radhey'
#     course = 'BCom'
#     year = 1
#     sem = 1
#     address = "Uttam Nagar"

# student1 = Student()
# print(student1)
# print(student1.id)
# print(student1.name)
# print(student1.course)
# print(student1.year)
# print(student1.sem)
# print(student1.address)

# student1.address = "Rohini"

# print(student1.__dict__)

# print()
# print("Student2")

# student2 = Student()
# print(student2)
# print(student2.id)
# print(student2.name)
# print(student2.course)
# print(student2.year)
# print(student2.sem)
# print(student2.address)


class Student:
    id = None
    name = None
    course = 'BCom'
    year = None
    sem = None
    address = None

student1 = Student()

student1.id = 101
student1.name = "Radhey"
student1.year = 1
student1.sem = 1
student1.address = "Uttam Nagar" 

print(student1)
print(student1.id)
print(student1.name)
print(student1.course)
print(student1.year)
print(student1.sem)
print(student1.address)

print(student1.__dict__)

print()
print("Student2")

student2 = Student()

student2.id = 102
student2.name = "Anmol"
student2.year = 3
student2.sem = 3
student2.address = "Rohini"
student2.course = "BCA" 

print(student2)
print(student2.id)
print(student2.name)
print(student2.course)
print(student2.year)
print(student2.sem)
print(student2.address)

print(student2.__dict__)