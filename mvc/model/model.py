class User:
    usersList = []

    def __init__(self, name, email, password):   #parameterized constructor
        self.name = name
        self.email = email
        self.password = password
        self.usersList.append(self)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.password}"

def register(name,email,password):
    user = User(name,email,password)
    return user.usersList