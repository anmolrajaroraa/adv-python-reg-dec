import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCJXmelfj-0zMG5ktmLXhVymJIjWvUpu50",
    "authDomain": "testproject-anmol.firebaseapp.com",
    "databaseURL": "https://testproject-anmol.firebaseio.com",
    "projectId": "testproject-anmol",
    "storageBucket": "testproject-anmol.appspot.com",
    "messagingSenderId": "358944694097",
    "appId": "1:358944694097:web:a68a49131fc0887a3e3d70"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
users = db.child("users/1/posts/1/post").get()
print(users.val())