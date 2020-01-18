import mws, os

count = 1

orders_api = mws.Orders(
        access_key=os.environ['MWS_ACCESS_KEY'],
        secret_key=os.environ['MWS_SECRET_KEY'],
        account_id=os.environ['MWS_ACCOUNT_ID']
        )
marketplace_ca = 'A2EUQ1WTGCTBG2'

response = orders_api.list_orders(marketplaceids=[marketplace_ca], created_after='2019-01-01').parsed
orders_list = response['Orders']['Order']

for o in orders_list:
    print(str(count) + ": " + o['AmazonOrderId']['value'])
    count = count + 1

while('NextToken' in response):
    next_token = response['NextToken']['value']
    response = orders_api.list_orders_by_next_token(next_token).parsed
    orders_list = response['Orders']['Order']

    for o in orders_list:
        print(str(count) + ": " + o['AmazonOrderId']['value'])
        count = count + 1


