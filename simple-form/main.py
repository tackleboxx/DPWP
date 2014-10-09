'''
name
date
class
assignment
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self): #function that starts
        p = Page()
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.title = "Simple Form"
        self.css = "css/main.css"
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self.body = '''<form method="GET" action="">
        <label>First Name:</label><input type="text" name="fname" />
        <label>Last Name:</label><input type="text" name="lname" />
        <label>Address:</label><input type="text" name="address" />
        <label>City:</label><input type="text" name="city" />
        <label>State:</label><input type="text" name="state" />
        <label>Zipcode:</label><input type="text" name="zipcode" />
        <label>Email:</label><input type="text" name="email" />
        <input type="submit" value="submit" />'''

        self.close = '''
        </form>
    </body>
</html>'''

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

#never touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
