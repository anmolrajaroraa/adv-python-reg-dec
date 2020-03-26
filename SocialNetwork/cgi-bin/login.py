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


def newsFeed(firstname, email):
    base.newsFeedStart()
    posts = model.getPosts(firstname, email)
    for post in posts:
        base.newsFeedPost(post)
    base.newsFeedEnd()


if caption != None:
    media = fieldStorage["media"]
    model.savePost(email, caption, media)

if firstname != None:
    base.navbar(firstname, email)
    newsFeed(firstname, email)
else:
    password = fieldStorage.getvalue("password")
    result = model.login(email, password)
    if isinstance(result, model.User):
        base.navbar(result.firstname, result.email)
        newsFeed(result.firstname, result.email)
    else:
        base.error(email, "Invalid Credentials !")

base.footer()

# print(f'''
# Email : {email}
# Password : {password}
# ''')
