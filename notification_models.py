from google.appengine.ext import ndb
import datetime

class Notification(ndb.Model):
    target_time = ndb.DateTimeProperty(required=True)
    stop_name = ndb.StringProperty(required=True)
    sent = ndb.BooleanProperty(default=False)
