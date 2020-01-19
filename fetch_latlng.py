import os
import googlemaps
import pandas as pd
import pprint

gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAP_API'])

data = []

df = pd.read_csv('orders.csv')
for index, row in df.iterrows(): 
    # Geocoding an address
    address = row['City'] + ' ' + row['StateOrRegion'] + ' ' + row['PostalCode'] + ' ' + row['CountryCode']    
    geocode_result = gmaps.geocode(address)
    
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        data.append([
            row['OrderId'],
            lat,
            lng
        ])
    except IndexError:
        print("No result for " + row['OrderId'] + " - " + address)

df = pd.DataFrame(data, columns=['OrderId','lat','lng'])
print(df)

file_name = 'orders_latlng.csv'
print('Writing df into ' + file_name + ' ...')
df.to_csv(file_name, encoding='utf-8', index=False)
print('Writing complete...')



