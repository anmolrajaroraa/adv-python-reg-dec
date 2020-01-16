#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import DB, base, cgi

fieldStorage = cgi.FieldStorage()
category = fieldStorage.getvalue("category")

if category == None:
    base.header("Deals of the Day")
    for product in DB.products:
        base.createProduct(product)
else:
    base.header(category.upper())
    for product in DB.products:
        if category == product["product_category"]:
            base.createProduct(product)

base.footer()