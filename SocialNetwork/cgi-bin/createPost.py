#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base
import cgi

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")

base.header()
base.navbar(firstname, email)
base.createPostForm(firstname, email)
base.footer()
