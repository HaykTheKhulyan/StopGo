from google.appengine.ext import ndb

class Stop(ndb.Model):
    stop_id = ndb.StringProperty(required=True)
    stop_code = ndb.StringProperty(required=True)
    stop_name = ndb.StringProperty(required=True)
    stop_desc = ndb.StringProperty(required=False)
    stop_lat = ndb.StringProperty(required=True)
    stop_lon = ndb.StringProperty(required=True)
    stop_url = ndb.StringProperty(required=False)
    location_type = ndb.StringProperty(required=False)
    parent_station = ndb.StringProperty(required=False)
    tpis_name = ndb.StringProperty(required=False)
