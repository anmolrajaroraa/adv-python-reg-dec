#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

import DB, base, cgi

fieldStorage = cgi.FieldStorage()
query = fieldStorage.getvalue('q')
query = query.lower()

for category in DB.searchIntents.keys():
    if query in DB.searchIntents[category]:
        query = category

base.header(query.upper())

# print(query)

for product in DB.products:
    if query in product['product_sub_category'] or query in product['product_brand'].lower() or query in product['product_name'].lower() or query == product["product_category"]:
        base.createProduct(product)