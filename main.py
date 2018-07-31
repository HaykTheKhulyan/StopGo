import webapp2
import os
import jinja2
from math import sin, cos, sqrt, atan2, radians
from stop_models import Stop
from seed_stops_db import seed_data

#this is in mph
bus_speed = 26.4

jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

def find_time_to_stop(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(abs(lat1))
    lng1 = radians(abs(lng1))
    lat2 = radians(abs(lat2))
    lng2 = radians(abs(lng2))

    delta_lng = lng2 - lng1
    delta_lat = lat2 - lat1

    a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

class MainHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_env.get_template('templates/homepage.html')
        self.response.write(welcome_template.render())


class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()

class CreateRouteHandler(webapp2.RequestHandler):
    def get(self):
        create_route_template = jinja_env.get_template('templates/create_route.html')
        self.response.write(create_route_template.render())

class InformationHandler(webapp2.RequestHandler):
    def get(self):
        info_template = jinja_env.get_template('templates/information.html')
        self.response.write(info_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/seed-data', LoadDataHandler),
    ('/create-route', CreateRouteHandler),
    ('/info', InformationHandler),
], debug=True)
