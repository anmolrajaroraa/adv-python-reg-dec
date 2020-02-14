#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import model
import base
import cgi
print("Content-type: text/html\r\n\r\n")


base.header()

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")
caption = fieldStorage.getvalue("caption")
media = fieldStorage.getvalue("media")

if caption != None:
    media = fieldStorage["media"]
    model.savePost(email, caption, media)

if firstname != None:
    base.navbar(firstname, email)
    base.newsFeedStart()
    base.newsFeedPost()
    base.newsFeedEnd()
else:
    password = fieldStorage.getvalue("password")
    result = model.login(email, password)
    if isinstance(result, model.User):
        base.navbar(result.firstname, result.email)
        base.newsFeedStart()
        base.newsFeedPost()
        base.newsFeedEnd()
    else:
        base.error(email, "Invalid Credentials !")

base.footer()

# print(f'''
# Email : {email}
# Password : {password}
# ''')
