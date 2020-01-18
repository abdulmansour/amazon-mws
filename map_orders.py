import mws, os, pprint
import pandas as pd 

data = []

def main():
    orders_api = mws.Orders(
        access_key=os.environ['MWS_ACCESS_KEY'],
        secret_key=os.environ['MWS_SECRET_KEY'],
        account_id=os.environ['MWS_ACCOUNT_ID']
        )
    marketplace_ca = 'A2EUQ1WTGCTBG2'

    print('Fetching Orders data...')

    response = orders_api.list_orders(marketplaceids=[marketplace_ca], created_after='2019-01-01').parsed
    append_address_info(response)

    while('NextToken' in response):
        next_token = response['NextToken']['value']
        response = orders_api.list_orders_by_next_token(next_token).parsed
        append_address_info(response)

    print('Done fetching Orders data...')   

    df = pd.DataFrame(data, columns=['OrderId','City','CountryCode','PostalCode','StateOrRegion'])
    print(df)

def append_address_info(response):
    orders_list = response['Orders']['Order']
    for o in orders_list:
        if ('ShippingAddress' in o):
            data.append([
                o['AmazonOrderId']['value'], 
                o['ShippingAddress']['City']['value'],
                o['ShippingAddress']['CountryCode']['value'],
                o['ShippingAddress']['PostalCode']['value'],
                o['ShippingAddress']['StateOrRegion']['value'],
            ])

if __name__ == "__main__":
    main()
