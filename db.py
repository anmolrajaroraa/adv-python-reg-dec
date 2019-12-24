#pip install pymysql
import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='mvc', user='root', autocommit=True)

cursor = connection.cursor()

# Code for registration
query = f"insert into users (username, email, password) values ('{name}', '{email}', '{password}')"
result = cursor.execute(query)
print(result)

#Code for login
# query = "select username, email, password from users where email = 'ram@gmail.com' and password = 'ram12345' "
# result = cursor.execute(query)
# if result == 1:
#     data = cursor.fetchall()
#     userObj = User(data[0], data[1], data[2])
#     return userObj
# else:
#     return "Invalid credentials"
# print(result)
# print(data)