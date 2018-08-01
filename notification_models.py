from google.appengine.ext import ndb
import datetime

class Notification(ndb.Model):
    target_time = ndb.DateTimeProperty(required=True)
    sent = ndb.BooleanProperty(required=False)
