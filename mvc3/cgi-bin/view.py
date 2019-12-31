#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

def loginSuccessful(userObject):
    print(f'''
    <h1>Welcome {userObject.name}</h1>
    ''')

def loginFailure(message):
    print(f'''
    <h1>{message}</h1>
    ''')

def registerSuccessful(userObject):
    print(f'''
    <h1>Welcome {userObject.name}</h1>
    ''')

def registerFailure(message):
    print(f'''
    <h1>{message}</h1>
    ''')