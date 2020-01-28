import mws, os
import pandas as pd
import time

data = []

def main():
    orders_api = mws.Orders(
        access_key=os.environ['MWS_ACCESS_KEY'],
        secret_key=os.environ['MWS_SECRET_KEY'],
        account_id=os.environ['MWS_ACCOUNT_ID']
        )
    marketplace_ca = 'A2EUQ1WTGCTBG2'
    marketplace_us = 'ATVPDKIKX0DER'

    print('Fetching Orders data...')

    response = orders_api.list_orders(marketplaceids=[marketplace_ca, marketplace_us], created_after='2017-01-01').parsed
    append_info(response)

    while('NextToken' in response):
        try:
            next_token = response['NextToken']['value']
            response = orders_api.list_orders_by_next_token(next_token).parsed
            append_address_info(response)

        except:
            print("503 Server Error: Service Unavailable to process url. Will try again...")
            time.sleep(1)

    print('Done fetching Orders data...')

    df = pd.DataFrame(data, columns=[
        'AmazonOrderId',
        'BuyerEmail',
        'NumberOfItemsShipped',
        'OrderStatus','Amount',
        'PurchaseDate',
        'ShipServiceLevel',
        'IsPrime',
        'City',
        'Country',
        'PostalCode',
        'StateOrRegion'
    ])
    print(df)

    file_name = 'orders_full_details.csv'
    print('Writing df into ' + file_name + ' ...')
    df.to_csv(file_name, encoding='utf-8', index=False)
    print('Writing complete...')

#append order address info into data list    
def append_info(response):
    print(response['NextToken'])
    orders_list = response['Orders']['Order']
    for o in orders_list:
        data_dict = {}

        if 'AmazonOrderId' in o:
           data_dict['AmazonOrderId'] = o['AmazonOrderId']['value']
        else:
            data_dict['AmazonOrderId'] = 'null'

        if 'BuyerEmail' in o:
            data_dict['BuyerEmail'] = o['BuyerEmail']['value']
        else:
            data_dict['BuyerEmail'] = 'null'

        if 'NumberOfItemsShipped' in o:
            data_dict['NumberOfItemsShipped'] = o['NumberOfItemsShipped']['value'] 
        else:
            data_dict['NumberOfItemsShipped'] = 'null'

        if 'OrderStatus' in o:
            data_dict['OrderStatus'] = o['OrderStatus']['value'] 
        else:
            data_dict['OrderStatus'] = 'null'

        if 'OrderTotal' in o:
            data_dict['Amount'] = o['OrderTotal']['Amount']['value']
        else:
            data_dict['Amount'] = 'null'

        if 'PurchaseDate' in o:
            data_dict['PurchaseDate'] = o['PurchaseDate']['value']
        else:
            data_dict['PurchaseDate'] = 'null'
        
        if 'ShipServiceLevel' in o:
            data_dict['ShipServiceLevel'] = o['ShipServiceLevel']['value']
        else:
            data_dict['ShipServiceLevel'] = 'null'

        if 'IsPrime' in o:
            data_dict['IsPrime'] = o['IsPrime']['value']
        else:
            data_dict['IsPrime'] = 'null'

        if 'ShippingAddress' in o:
            if 'City' in o['ShippingAddress']:
                data_dict['City'] = o['ShippingAddress']['City']['value']
        else:
            data_dict['City'] = 'null'

        if 'ShippingAddress' in o:
            if 'CountryCode' in o['ShippingAddress']:
                data_dict['Country'] = o['ShippingAddress']['CountryCode']['value']
        else:
            data_dict['Country'] = 'null'

        if 'ShippingAddress' in o:
            if 'PostalCode' in o['ShippingAddress']:
                data_dict['PostalCode'] = o['ShippingAddress']['PostalCode']['value']
        else:
            data_dict['PostalCode'] = 'null'

        if 'ShippingAddress' in o:
            if 'StateOrRegion' in o['ShippingAddress']:
                data_dict['StateOrRegion'] = o['ShippingAddress']['StateOrRegion']['value']
        else:
            data_dict['StateOrRegion'] = 'null'

        data.append([
            data_dict['AmazonOrderId'],
            data_dict['BuyerEmail'],
            data_dict['NumberOfItemsShipped'], 
            data_dict['OrderStatus'],
            data_dict['Amount'],
            data_dict['PurchaseDate'], 
            data_dict['ShipServiceLevel'],
            data_dict['IsPrime'],
            data_dict['City'],
            data_dict['Country'],
            data_dict['PostalCode'],
            data_dict['StateOrRegion']
        ])

if __name__ == "__main__":
    main()
