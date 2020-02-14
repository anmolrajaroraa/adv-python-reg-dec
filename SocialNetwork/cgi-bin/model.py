import pymysql
import os

connection = pymysql.connect(
    host="localhost", user="root", database="socialhub", port=3306, autocommit=True)

cursor = connection.cursor()


class User:
    def __init__(self, firstname, lastname, email, password, birthday, gender):
        self.firstname = firstname
        self.lastname = lastname if lastname != None else ''
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender


class ProfileDetails:
    def __init__(self, data):
        data = list(data)
        for i in range(len(data)):
            if data[i] == None:
                data[i] = ''
        self.profile_pic = data[1]
        self.bio = data[2]
        self.nickname = data[3]
        self.workplace = data[4]
        self.skills = data[5]
        self.university = data[6]
        self.school = data[7]
        self.current_city = data[8]
        self.hometown = data[9]
        self.other_places = data[10]
        self.contact = data[11]
        self.relationship_status = data[12]


def register(firstname, lastname, email, password, birthday, gender):
    userObject = User(firstname, lastname, email, password, birthday, gender)
    query = "insert into users values (%s,%s,%s,%s,%s,%s)"
    result = cursor.execute(query, (userObject.firstname, userObject.lastname,
                                    userObject.email, userObject.password, userObject.birthday, userObject.gender))
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
    profileObject = ProfileDetails((email, None, bio, nickname, workplace, skills, university,
                                    school, current_city, hometown, other_places, contact, relationship_status))
    query = "update profile_details set bio = %s, nickname = %s, workplace = %s, skills = %s, university = %s, school = %s, current_city = %s, hometown = %s, other_places = %s, contact = %s, relationship_status = %s where email = %s"
    cursor.execute(query, (profileObject.bio, profileObject.nickname, profileObject.workplace, profileObject.skills, profileObject.university, profileObject.school,
                           profileObject.current_city, profileObject.hometown, profileObject.other_places, profileObject.contact, profileObject.relationship_status, email))


def updateProfilePic(email, profile_pic):
    open(f'images/{profile_pic.filename}', 'wb').write(profile_pic.file.read())
    query = "update profile_details set profile_pic = %s where email = %s"
    cursor.execute(query, (profile_pic.filename, email))


def getProfileDetails(email):
    query = "select * from profile_details where email = %s"
    result = cursor.execute(query, (email))
    if result == 1:
        data = cursor.fetchone()
        return ProfileDetails(data)


def getUserDetails(email):
    query = "select firstname, lastname, birthday, gender from users where email = %s"
    result = cursor.execute(query, (email))
    if result == 1:
        data = cursor.fetchone()
        return User(data[0], data[1], email, None, data[2], data[3])


def getFriendsList(email):
    query = "select friend_name from friends where email = %s"
    result = cursor.execute(query, (email))
    if result > 0:
        data = cursor.fetchall()
        # print(data)
        return data


def getAllFriends(email):
    query = "select distinct friend_name from friends where friend_name not in (select friend_name from friends where email = %s)"
    result = cursor.execute(query, (email))
    if result > 0:
        data = cursor.fetchall()
        # print(data)
        return data


def addFriend(email, friend_name):
    query = "insert into friends values (%s, %s)"
    cursor.execute(query, (email, friend_name))


def savePost(email, caption, media):
    media_name = None
    if len(media.filename) > 0:
        media_name = media.filename
        open(f'images/{media_name}', 'wb').write(media.file.read())
    query = "insert into posts (email, caption, media_link, likes, comments, shares) values (%s, %s, %s, 0, 0, 0)"
    cursor.execute(query, (email, caption, media_name))
