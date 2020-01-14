#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import base, cgi, DB

fieldStorage = cgi.FieldStorage()
pid = int(fieldStorage.getvalue("pid"))

base.header("Product")

for product in DB.products:
    if product["product_id"] == pid:
        base.createHorizontalProduct(product)
        break

base.footer()