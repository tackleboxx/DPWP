'''
name
date
class
assignment
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self): #function that starts
<<<<<<< HEAD

        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>'''


        page_body = '''<form method="GET" action="">
        <label>Name:</label><input type="text" name="user" />
        <label>Email:</label><input type="text" name="email" />
        <input type="submit" value="submit" />'''

        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we get from form
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #printing page out
=======
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
        <label>Name:</label><input type="text" name="user" />
        <label>Email:</label><input type="text" name="email" />
        <input type="submit" value="submit" />
        </form>
    </body>
</html>'''
        self.response.write(page)
>>>>>>> FETCH_HEAD
        #code go here

    def additional_functions(self):
        pass
        #code go here


#never touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
