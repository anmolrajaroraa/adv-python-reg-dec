#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, model

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")

base.header()
base.navbar(firstname,email)
base.editProfileForm(firstname,email)
base.footer()