#pip install pymysql
import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='mvc', user='root', autocommit=True)

cursor = connection.cursor()

query = "insert into users (username, email, password) values ('mohan', 'mohan@gmail.com', 'mohan1234')"
result = cursor.execute(query)
print(result)