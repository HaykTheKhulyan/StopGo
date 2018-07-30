from stop_models import Stop
import csv

def seed_data():
    with open('stops.txt') as csvfile:
         stopreader = csv.DictReader(csvfile)
         for row in stopreader:
             Stop(stop_id=row['stop_id'], stop_code=row['stop_code'], \
             stop_name=row['stop_name'],stop_desc=row['stop_desc'], \
             stop_lat=row['stop_lat'], stop_lon=row['stop_lon'],\
             stop_url=row['stop_url'], location_type=row['location_type'], \
             parent_station=row['parent_station'], tpis_name=row['tpis_name']).put()


            
