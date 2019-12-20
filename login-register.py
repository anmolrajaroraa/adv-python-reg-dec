class User:
    users = []

    def __init__(self, name, email, password):   #parameterized constructor
        self.name = name
        self.email = email
        self.password = password
        self.users.append(self)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.password}"

def login():
    pass

def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    userObj = User(name,email,password)
    for user in userObj.users:
        print(user)

print('''
1. Login
2. Register
''')
choice = input("Enter your choice: ")
options = {'1' : login, '2': register}
options[choice]()