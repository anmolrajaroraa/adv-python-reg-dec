#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi
import base
import model

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")
flag = fieldStorage.getvalue("friend")

base.header()
base.navbar(firstname, email)
base.createFriendsList()

if flag != "all" and flag != None:
    model.addFriend(email, flag)

friends = model.getFriendsList(email)

if flag == "all":
    for friend in model.getAllFriends(email):
        base.createFindFriendLi(friend[0], firstname, email)
else:
    for friend in friends:
        base.createLi(friend[0])

base.endFriendsList()
base.footer()
