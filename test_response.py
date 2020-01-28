import mws, os, pprint

orders_api = mws.Orders(
        access_key=os.environ['MWS_ACCESS_KEY'],
        secret_key=os.environ['MWS_SECRET_KEY'],
        account_id=os.environ['MWS_ACCOUNT_ID']
        )
marketplace_ca = 'A2EUQ1WTGCTBG2'
marketplace_us = 'ATVPDKIKX0DER'

response = orders_api.list_orders(marketplaceids=[marketplace_ca, marketplace_us], created_after='2019-01-01').parsed

pprint.pprint(response)
