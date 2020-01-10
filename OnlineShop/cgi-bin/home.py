#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import DB, base

base.header()

for product in DB.products:
    base.createProduct(product)

base.footer()