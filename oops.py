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


class StudentClass:
    '''This class is used to create objects of students'''
    
    students = [] #this list will be global for all the objects (means it will be shared with all the objects)

    def __init__(self):   #constructor
        self.id = None
        self.name = None
        self.course = 'BCom'
        self.year = None
        self.sem = None
        self.address = None
        self.student_details = []  #unique to a single object

    def __str__(self):  #magic method - gets invoked (Call) automatically when we try to print the object
        print("Student details -",self.student_details)
        print("Students are",self.students)
        return f"Id is {self.id}, Name is {self.name}, Course is {self.course}, Year is {self.year}, Sem is {self.sem}, Address is {self.address}"

    def showDetails(self):  #self means the current owner of the functions or the object which called the function
        print(self.id, self.name, self.course, self.year, self.sem, self.address)

    def fillDetailsInList(self):
        self.students.append( [self.id,self.name,self.course,self.year,self.sem,self.address] )
        self.student_details.append( [self.id,self.name,self.course,self.year,self.sem,self.address] )

student1Object = StudentClass()

student1Object.id = 101
student1Object.name = "Radhey"
student1Object.year = 1
student1Object.sem = 1
student1Object.address = "Uttam Nagar" 
student1Object.fillDetailsInList()
print(student1Object)

# print(student1Object)
# print(student1Object.id)
# print(student1Object.name)
# print(student1Object.course)
# print(student1Object.year)
# print(student1Object.sem)
# print(student1Object.address)

# print(student1Object.__dict__)

# print()
# print("Student2")

student2Object = StudentClass()

student2Object.id = 102
student2Object.name = "Anmol"
student2Object.year = 3
student2Object.sem = 3
student2Object.address = "Rohini"
student2Object.course = "BCA" 
student2Object.fillDetailsInList()
print(student2Object)

# print(student2Object)
# print(student2Object.id)
# print(student2Object.name)
# print(student2Object.course)
# print(student2Object.year)
# print(student2Object.sem)
# print(student2Object.address)

# print(student2Object.__dict__)  #returns a dictionary containing all the modified values
# print(student2Object.__dir__()) #shows us all the properties and methods available with the object
# print(student2Object.__doc__) #show the documentation string for the object's class
# print(student2Object.__class__) #shows the name of the class
# print(type(student2Object))
# print(isinstance(student2Object, StudentClass))
# student2Object.showDetails()
# student1Object.showDetails()
# print(student1Object)  #calls __str__ method automatically
# print(student2Object)