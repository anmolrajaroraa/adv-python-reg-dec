#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# import model
import sys
import cgi
print("Content-type: text/html\r\n\r\n")


# print("AJAX call received...")
fieldStorage = cgi.FieldStorage()
email = fieldStorage.getvalue('email')
# msg = model.validateEmail(email)
# sys.stdout.write("Content-Type : text/plain")
sys.stdout.write("Invalid email")
