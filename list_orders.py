import mws, os

count = 1

def main():
    orders_api = mws.Orders(
            access_key=os.environ['MWS_ACCESS_KEY'],
            secret_key=os.environ['MWS_SECRET_KEY'],
            account_id=os.environ['MWS_ACCOUNT_ID']
            )
    marketplace_ca = 'A2EUQ1WTGCTBG2'

    response = orders_api.list_orders(marketplaceids=[marketplace_ca], created_after='2019-01-01').parsed
    print_orders(response)

    while('NextToken' in response):
        try:
            next_token = response['NextToken']['value']
            response = orders_api.list_orders_by_next_token(next_token).parsed
            print_orders(response)
        except:
            print("503 Server Error: Service Unavailable to process url. Will try again...")
            time.sleep(1)


def print_orders(response):
    global count
    orders_list = response['Orders']['Order']
    for o in orders_list:
        print(str(count) + ": " + o['AmazonOrderId']['value'])
        count = count + 1


if __name__ == "__main__":
    main()
