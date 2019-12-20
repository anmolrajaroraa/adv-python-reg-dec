import sys
sys.path.append('..')
from controller import controller

def login():
    pass

def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    usersList = controller.register(name,email,password)
    for user in usersList:
        print(user)

print('''
1. Login
2. Register
''')
choice = input("Enter your choice: ")
options = {'1' : login, '2': register}
options[choice]()