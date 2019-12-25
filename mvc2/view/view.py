import sys 
sys.path.append('..')
from controller import controller
import pymysql
from model.model import User

def dashboard(user):

    def createPost():
        pass

    def viewProfile():
        pass

    def updateProfile():
        pass

    while True:
        print('''
        1. Create Post
        2. View Profile
        3. Update Profile
        4. Logout
        ''')
        choice = input("Enter your choice: ")
        if choice == "4":
            return
        options = {"1": createPost, "2": viewProfile, "3": updateProfile}
        options[choice]()

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = controller.login(email,password)
    if isinstance(result, User):
        print("Welcome " + result.name)
        dashboard(result)
    else:
        print(result)

def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    result = controller.register(name,email,password)
    if isinstance(result, User):
        print("Registration successful")
        dashboard(result)
    else:
        print(result)

while True:
    print('''
    1. Login
    2. Register
    3. Exit
    ''')
    try:
        choice = input("Enter your choice: ")
        if choice == "3":
            break
        options = {'1' : login, '2': register}
        options[choice]()
    except pymysql.err.IntegrityError:
        print("Email already exists! Please use another email or try logging in!")
    except BaseException as error:
        print(error)