import webapp2
import os
import jinja2
import json
import datetime
from math import sin, cos, sqrt, atan2, radians
from stop_models import Stop
from notification_models import Notification
#from seed_stops_db import seed_data
from twilio.rest import Client
from google.appengine.ext import ndb
import logging

my_file = open("app-secrets.json")
my_secret = my_file.read()
SECRETS_DICT = json.loads(my_secret)
my_file.close()


jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

stop_name = ""

#returns time in minutes (this is always an underestimate, moreso for longer routes)
def find_time_to_stop(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    R = 6373.0
    bus_speed = 26.4

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

def SendNotification(Notification, myStop):
    account_sid = SECRETS_DICT['twilio_account_sid']
    auth_token  = SECRETS_DICT['twilio_auth_token']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12136047704",
        from_="+14243583569",
        body="Your stop at %s is coming up!" % Notification.stop_name)

    print(message.sid)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_page_template = jinja_env.get_template('templates/homepage.html')
        self.response.write(main_page_template.render(()))

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()

class CreateRouteHandler(webapp2.RequestHandler):
    def get(self):
        create_route_template = jinja_env.get_template('templates/create_route.html')
        logging.error("CreateRouteHandler")
        self.response.write(create_route_template.render(()))

class ViewRouteHandler(webapp2.RequestHandler):
    def get(self):
        view_route_template = jinja_env.get_template('templates/view_route.html')

        current_stop = self.request.get('current_stop')
        next_stop = self.request.get('next_stop')

        stop_name = current_stop

        current_stop_lat = Stop.query().filter(Stop.stop_name == current_stop).fetch()[0].stop_lat
        current_stop_lon = Stop.query().filter(Stop.stop_name == current_stop).fetch()[0].stop_lon

        next_stop_lat = Stop.query().filter(Stop.stop_name == next_stop).fetch()[0].stop_lat
        next_stop_lon = Stop.query().filter(Stop.stop_name == next_stop).fetch()[0].stop_lon

        time_to_next_stop = find_time_to_stop(current_stop_lat, current_stop_lon, next_stop_lat, next_stop_lon)

        time_to_next_stop = float(int(time_to_next_stop * 10))
        time_to_next_stop /=10

        notification = Notification(target_time = datetime.datetime.now() + datetime.timedelta(minutes=time_to_next_stop), stop_name = next_stop).put()

        template_vars = {
            'time_to_next_stop': time_to_next_stop,
        }
        self.response.write(view_route_template.render(template_vars))

class InformationHandler(webapp2.RequestHandler):
    def get(self):
        info_template = jinja_env.get_template('templates/information.html')
        self.response.write(info_template.render())

class NotificationHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Cron is working")
        two_minutes_ago = (datetime.datetime.now() + datetime.timedelta(minutes=2))
        notifications = Notification.query(Notification.target_time <= datetime.datetime.now()).fetch()
        for notification in notifications:
            logging.error("Notification sent")
            SendNotification(notification, stop_name)
            notifications.sent = True
            notifications.put()

class OnRouteHandler(webapp2.RequestHandler):
    def get(self):
        on_route_template = jinja_env.get_template('templates/on_route.html')
        self.response.write(on_route_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/seed-data', LoadDataHandler),
    ('/create-route', CreateRouteHandler),
    ('/view-route', ViewRouteHandler),
    ('/info', InformationHandler),
    ('/notifier', NotificationHandler),
    ('/on-route', OnRouteHandler),
], debug=True)
