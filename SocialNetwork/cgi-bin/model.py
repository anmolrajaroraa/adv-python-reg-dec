import pymysql, os

connection = pymysql.connect(host="localhost", user="root", database="socialhub", port=3306, autocommit=True)

cursor = connection.cursor()

class User:
    def __init__(self, firstname, lastname, email, password, birthday, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender

class ProfileDetails:
    def __init__(self, bio, nickname, workplace, skills, university, school, current_city, hometown, other_places, contact, relationship_status):
        self.bio = bio
        self.nickname = nickname
        self.workplace = workplace
        self.skills = skills
        self.university = university
        self.school = school
        self.current_city = current_city
        self.hometown = hometown
        self.other_places = other_places
        self.contact = contact
        self.relationship_status = relationship_status

def register(firstname, lastname, email, password, birthday, gender):
    userObject = User(firstname, lastname, email, password, birthday, gender)
    query = "insert into users values (%s,%s,%s,%s,%s,%s)"
    result = cursor.execute(query, (userObject.firstname, userObject.lastname, userObject.email, userObject.password, userObject.birthday, userObject.gender))
    return result

def createProfile(email):
    query = "insert into profile_details (email, profile_pic) values (%s, 'default.png')"
    result = cursor.execute(query, (email))
    return result

def login(email, password):
    query = "select * from users where email = %s and password = %s"
    result = cursor.execute(query, (email, password))
    if result == 1:
        data = cursor.fetchone()
        userObject = User(data[0], data[1], data[2], None, data[4], data[5])
        return userObject

def updateProfile(email, bio, nickname, workplace, skills, university, school, current_city, hometown, other_places, contact, relationship_status):
    profileObject = ProfileDetails(bio, nickname, workplace, skills, university, school, current_city, hometown, other_places, contact, relationship_status)
    # if profile_pic.filename:
    #     image_data = profile_pic.file.read()
    #     open(f'images/{profile_pic.filename}', 'wb').write(image_data)
    query = "update profile_details set bio = %s, nickname = %s, workplace = %s, skills = %s, university = %s, school = %s, current_city = %s, hometown = %s, other_places = %s, contact = %s, relationship_status = %s where email = %s"
    result = cursor.execute(query, (profileObject.bio, profileObject.nickname, profileObject.workplace, profileObject.skills, profileObject.university, profileObject.school, profileObject.current_city, profileObject.hometown, profileObject.other_places, profileObject.contact, profileObject.relationship_status, email))
    return result