#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, model, view

fieldStorageObject = cgi.FieldStorage()
email = fieldStorageObject.getvalue("email")
password = fieldStorageObject.getvalue("password")

result = model.login(email,password)
if isinstance(result, model.User):
    view.loginSuccessful(result)
else:
    view.loginFailure(result)