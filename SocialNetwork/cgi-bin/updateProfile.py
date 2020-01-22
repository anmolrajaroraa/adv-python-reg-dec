#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base

fieldStorage = cgi.FieldStorage()
profile_pic = fieldStorage.getvalue("profile_pic")

base.header()
base.navbar("Ram", "ram@gmail.com")

print(profile_pic)