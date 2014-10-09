'''
name
date
class
assignment
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self): #function that starts
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
        <label>Name:</label><input type="text" />
        <label>Email:</label><input type="text" />
        </form>
    </body>
</html>'''
        self.response.write(page)
        #code go here

    def additional_functions(self):
        pass
        #code go here


#never touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
