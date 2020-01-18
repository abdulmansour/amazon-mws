import os
import googlemaps
import pandas as pd
import pprint

gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAP_API'])

df = pd.read_csv('orders.csv')

address_list = []
for index, row in df.iterrows():
    address_list.append(row['City'] + ' ' + row['StateOrRegion'] + ' ' + row['PostalCode'] + ' ' + row['CountryCode'])

pprint.pprint(address_list)

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#print(geocode_result)

