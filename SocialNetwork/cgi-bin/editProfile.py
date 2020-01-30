#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, model

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue("firstname")
email = fieldStorage.getvalue("email")

base.header()
base.navbar(firstname,email)
result = model.getProfileDetails(email)
base.editProfileForm(firstname,email, result)
base.profilePicModal(firstname,email)
base.runScript(result.relationship_status)
base.footer()