#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi, model

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
lastname = fieldStorage.getvalue("lastname")
email = fieldStorage.getvalue("email")
password = fieldStorage.getvalue("password")
birthday = fieldStorage.getvalue("birthday")
gender = fieldStorage.getvalue("gender")

# print(f'''
# Firstname : {firstname}
# Lastname : {lastname}
# Email : {email}
# Password : {password}
# Birthday : {birthday}
# Gender : {gender}
# ''')

result = model.register(firstname, lastname, email, password, birthday, gender)