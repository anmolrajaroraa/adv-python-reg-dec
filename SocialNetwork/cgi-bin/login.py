#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi, base, model

fieldStorage = cgi.FieldStorage()
email = fieldStorage.getvalue("email")
password = fieldStorage.getvalue("password")

# print(f'''
# Email : {email}
# Password : {password}
# ''')

base.header()
result = model.login(email, password)
if isinstance(result, model.User):
    base.navbar(result.firstname)
else:
    base.error(email, "Invalid Credentials !")
base.footer()