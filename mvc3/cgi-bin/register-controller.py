#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, model, view

fieldStorageObject = cgi.FieldStorage()
name = fieldStorageObject.getvalue("username")
email = fieldStorageObject.getvalue("email")
password = fieldStorageObject.getvalue("password")

result = model.register(name,email,password)
if isinstance(result, model.User):
    view.registerSuccessful(result)
else:
    view.registerFailure(result)