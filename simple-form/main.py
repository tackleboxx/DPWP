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
        <label>State:</label><select name="state" size="1">
            <option selected value="">State...</option>
            <option value="ZZ">None</option>
            <option value="">-- UNITED STATES --</option>
            <option value="AL">Alabama</option>
            <option value="AK">Alaska</option>
            <option value="AZ">Arizona</option>
            <option value="AR">Arkansas</option>
            <option value="CA">California</option>
            <option value="CO">Colorado</option>
            <option value="CT">Connecticut</option>
            <option value="DE">Delaware</option>
            <option value="FL">Florida</option>
            <option value="GA">Georgia</option>
            <option value="HI">Hawaii</option>
            <option value="ID">Idaho</option>
            <option value="IL">Illinois</option>
            <option value="IN">Indiana</option>
            <option value="IA">Iowa</option>
            <option value="KS">Kansas</option>
            <option value="KY">Kentucky</option>
            <option value="LA">Louisiana</option>
            <option value="ME">Maine</option>
            <option value="MD">Maryland</option>
            <option value="MA">Massachusetts</option>
            <option value="MI">Michigan</option>
            <option value="MN">Minnesota</option>
            <option value="MS">Mississippi</option>
            <option value="MO">Missouri</option>
            <option value="MT">Montana</option>
            <option value="NE">Nebraska</option>
            <option value="NV">Nevada</option>
            <option value="NH">New Hampshire</option>
            <option value="NJ">New Jersey</option>
            <option value="NM">New Mexico</option>
            <option value="NY">New York</option>
            <option value="NC">North Carolina</option>
            <option value="ND">North Dakota</option>
            <option value="OH">Ohio</option>
            <option value="OK">Oklahoma</option>
            <option value="OR">Oregon</option>
            <option value="PA">Pennsylvania</option>
            <option value="RI">Rhode Island</option>
            <option value="SC">South Carolina</option>
            <option value="SD">South Dakota</option>
            <option value="TN">Tennessee</option>
            <option value="TX">Texas</option>
            <option value="UT">Utah</option>
            <option value="VT">Vermont</option>
            <option value="VA">Virginia</option>
            <option value="WA">Washington</option>
            <option value="WV">West Virginia</option>
            <option value="WI">Wisconsin</option>
            <option value="WY">Wyoming</option>
</select>

        <label>Zipcode:</label><input type="text" name="zipcode" />
        <label>Email:</label><input type="text" name="email" />
        <input type="checkbox" name="vehicle" name="checkbox">Agree To Terms
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
