#!/usr/local/bin/python3.7
import cgi
print("Content-type: text/html\r\n\r\n")
print("""<head>
<title>Style Sheet Sample</title>
<style TYPE="text/css">
<link rel="stylesheet" type="text/css" href="sample.css">
</style>
</head>""")
print("<html><body>")
print("<h1> Hello Program! </h1>")

print("<form  method = 'post' action = 'helloworld.py'>")
print("<p>Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")


form = cgi.FieldStorage()
if form.getvalue('name'):
    name = form.getvalue('name')
    print("<h1> Hello, " + name + "! Thank you!</h1><br/>")
if form.getvalue('happy'):
    print("<p> Yeah! I'm happy, too.</p>")
if form.getvalue('sad'):
    print("<p> Oh, No! What happened?</p>")

print("</body></html>")