import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='mvc', user='root', autocommit=True)

cursor = connection.cursor()


class User:

    def __init__(self, name, email, password):   #parameterized constructor
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.name}, {self.email}, {self.password}"

def register(name,email,password):
    user = User(name,email,password)
    query = f"insert into users (username, email, password) values (%s,%s,%s)"
    result = cursor.execute(query, (user.name, user.email, user.password))
    if result == 1:
        return "Registration successful"
    else:
        return "Unable to register at this moment!"

def login(email,password):
    query = "select username,email,password from users where email = %s and password = %s"
    result = cursor.execute(query, (email, password))
    if result == 1:
        data = cursor.fetchone()
        # print(data)
        user = User(data[0],data[1],data[2])
        return "Welcome " + user.name
    else:
        return "Invalid credentials"