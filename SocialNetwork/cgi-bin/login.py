#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi, base, model

base.header()

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")
if firstname != None:
    base.navbar(firstname, email)
else:
    password = fieldStorage.getvalue("password")
    result = model.login(email, password)
    if isinstance(result, model.User):
        base.navbar(result.firstname, result.email)
    else:
        base.error(email, "Invalid Credentials !")

base.footer()

# print(f'''
# Email : {email}
# Password : {password}
# ''')


