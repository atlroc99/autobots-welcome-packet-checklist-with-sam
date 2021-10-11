import json
import redis


def lambda_handler(event, context):
    # print('EVENT', event)
    dealership_name = event['pathParameters']['dealershipname']
    # TRIED rd = redis.Redis(host='docker.for.mac.localhost', port=6379)
    rd = redis.Redis(host='host.docker.internal', port=6379)

    is_redis_connected = False
    if rd.ping():
        is_redis_connected = rd.ping()
        print('redis connected')

    if is_redis_connected:
        dealer_checklist = json.loads(rd.get(dealership_name))
        print(dealer_checklist)

    response = {
        'statusCode': 200,
        'headers': {
            'content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({
            "dealershipName": dealership_name,
            "dealersChecklist": dealer_checklist
        })
    }

    return response
