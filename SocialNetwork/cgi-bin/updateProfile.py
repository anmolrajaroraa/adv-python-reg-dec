#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi, base, model, os

fieldStorage = cgi.FieldStorage()
firstname = fieldStorage.getvalue('firstname')
email = fieldStorage.getvalue('email')
# profile_pic = fieldStorage.getvalue("profile_pic")
profile_pic = fieldStorage['profile_pic']
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

base.header()
base.navbar(firstname, email)
# print(os.path.basename(profile_pic))
# print(profile_pic.filename)
model.updateProfile(email, profile_pic, bio, nickname, workplace, skills, university, school, current_city, hometown, other_places, contact, relationship_status)

# print(profile_pic)