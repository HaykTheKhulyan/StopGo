import webapp2
import os
import jinja2
from math import sin, cos, sqrt, atan2, radians
from stop_models import Stop
from seed_stops_db import seed_data

#this is in mph
bus_speed = 26.4

jina_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

#returns time in minutes (this is always an underestimate, moreso for longer routes)
def find_time_to_stop(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(abs(float(lat1)))
    lng1 = radians(abs(float(lng1)))
    lat2 = radians(abs(float(lat2)))
    lng2 = radians(abs(float(lng2)))

    delta_lng = lng2 - lng1
    delta_lat = lat2 - lat1

    a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    #distance in km
    distance = R * c

    #converts to miles
    distance = distance / 1.609344

    #converts distance to time required to get to the stop
    time_to_next_stop = distance * 60 / 24.6

    #multiplied by two since our model is ideal conditions
    return 2 * time_to_next_stop

class StopSelectorHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("Welcome to StopGo!")
        stop_selector_template = jina_env.get_template('templates/stop-selector.html')
        self.response.write(stop_selector_template.render())


class TestingHandler(webapp2.RequestHandler):
    def get(self):
        testing_template = jina_env.get_template('templates/testing.html')

        current_stop = self.request.get('current_stop')
        next_stop = self.request.get('next_stop')

        current_stop_lat = Stop.query().filter(Stop.stop_name == current_stop).fetch()[0].stop_lat
        current_stop_lon = Stop.query().filter(Stop.stop_name == current_stop).fetch()[0].stop_lon

        next_stop_lat = Stop.query().filter(Stop.stop_name == next_stop).fetch()[0].stop_lat
        next_stop_lon = Stop.query().filter(Stop.stop_name == next_stop).fetch()[0].stop_lon

        time_to_next_stop = find_time_to_stop(current_stop_lat, current_stop_lon, next_stop_lat, next_stop_lon)

        template_vars = {
            'time_to_next_stop': time_to_next_stop,
        }
        self.response.write(testing_template.render(template_vars))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()

app = webapp2.WSGIApplication([
    ('/', StopSelectorHandler),
    ('/testing', TestingHandler),
    ('/seed-data', LoadDataHandler),
], debug=True)
