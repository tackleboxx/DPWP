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
        <label>Name:</label><input type="text" name="user" />
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
