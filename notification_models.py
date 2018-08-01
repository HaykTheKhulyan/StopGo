from google.appengine.ext import ndb
import datetime

class Notification(ndb.Model):
    target_time = ndb.DateTimeProperty(required=True)
    sent = ndb.BooleanProperty(default=False)
    final_stop = ndb.StringProperty(required=True)
