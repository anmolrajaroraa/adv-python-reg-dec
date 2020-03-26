#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")
print('''<!DOCTYPE html>
<html>
    <head>
        <title>My First HTML Page</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        This is some text
        <h1 id="myHeading" class="htmlElement">This is some heading</h1>
        <p class="htmlElement">This is some paragraph</p>
        <h2>This is another heading</h2>
    </body>
</html>''')
