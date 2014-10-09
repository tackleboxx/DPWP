'''
name
date
class
assignment
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self): #function that starts
        self.response.write('Hello world!')
        #code go here

    def additional_functions(self):
        pass
        #code go here


#never touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
