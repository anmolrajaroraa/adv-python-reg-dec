import pymysql

connection = pymysql.connect(host="localhost", user="root", database="socialhub", port=3306, autocommit=True)

cursor = connection.cursor()

class User:
    def __init__(self, firstname, lastname, email, password, birthday, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender

def register(firstname, lastname, email, password, birthday, gender):
    userObject = User(firstname, lastname, email, password, birthday, gender)
    query = "insert into users values (%s,%s,%s,%s,%s,%s)"
    result = cursor.execute(query, (userObject.firstname, userObject.lastname, userObject.email, userObject.password, userObject.birthday, userObject.gender))
    return result