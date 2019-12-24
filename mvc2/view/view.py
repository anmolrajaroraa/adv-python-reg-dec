import sys
sys.path.append('..')
from controller import controller
import pymysql

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = controller.login(email,password)
    print(result)


def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = controller.register(name,email,password)
    print(result)

print('''
1. Login
2. Register
''')
try:
    choice = input("Enter your choice: ")
    options = {'1' : login, '2': register}
    options[choice]()
except pymysql.err.IntegrityError:
    print("Email already exists! Please use another email or try logging in!")
except BaseException as error:
    print(error)