#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import cgi, base, DB

fieldStorage = cgi.FieldStorage()
# pid = int(fieldStorage.getvalue("pid"))
pid = fieldStorage.getvalue("pid")

base.header("My Cart")

if pid != None:
    pid = int(pid)
    for product in DB.products:
        if pid == product["product_id"]:
            base.createProduct(product)

base.footer()