import folium
import pandas as pd
import json
from folium import plugins
import pgeocode

#df = pd.read_csv('orders.csv')

#with open('na.geo.json') as f:
#    naArea = json.load(f)
#    m = folium.Map(location[45.4819,-73.6421], zoom_start=11)
#    folium.GeoJson(naArea).add_to(m)

nomi = pgeocode.Nominatim('ca')
result = nomi.query_postal_code('J2C5B2')
print(result['latitude'])
print(result['longitude'])


