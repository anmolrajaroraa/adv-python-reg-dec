#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, model

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")

userObject = model.getUserDetails(email)
profileObject = model.getProfileDetails(email)

base.header()
base.navbar(firstname,email)
base.showProfile(userObject, profileObject)
base.footer()