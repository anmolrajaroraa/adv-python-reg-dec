#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, model, os

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue('firstname')
email = fieldStorage.getvalue('email')

base.header()
base.navbar(firstname, email)

if fieldStorage.getvalue("profile_pic") != None:
    profile_pic = fieldStorage['profile_pic'] 
    model.updateProfilePic(email, profile_pic)
    result = model.getProfileDetails(email)
    base.editProfileForm(firstname,email, result)
    base.profilePicModal(firstname,email)
    base.runScript(result.relationship_status)
else:
    bio = fieldStorage.getvalue('bio')
    nickname = fieldStorage.getvalue('nickname')
    workplace = fieldStorage.getvalue('workplace')
    skills = fieldStorage.getvalue('skills')
    university = fieldStorage.getvalue('university')
    school = fieldStorage.getvalue('school')
    current_city = fieldStorage.getvalue('current_city')
    hometown = fieldStorage.getvalue('hometown')
    other_places = fieldStorage.getvalue('other_places')
    contact = fieldStorage.getvalue('contact')
    relationship_status = fieldStorage.getvalue('relationship_status')
    model.updateProfile(email, bio, nickname, workplace, skills, university, school, current_city, hometown, other_places, contact, relationship_status)

base.footer()