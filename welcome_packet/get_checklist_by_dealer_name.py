import json
import redis
import os
import boto3
# from operator import itemgetter
# import ptvsd

# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()


# use of itemgetter: a,b = itemgetter(a,b)(py-dict)
current_region = os.environ.get('AWS_REGION')
print('Current region', current_region)
SSM = boto3.client('ssm', region_name=current_region)


def lambda_handler(event, context):
    print('\n*** Get dealer checklist by dealer_name')
    print('EVENT', event)
    # TRIED rd = redis.Redis(host='docker.for.mac.localhost', port=6379)
    rd = None
    dealership_name = event['pathParameters']['dealershipName']
    print('dealership_name:', dealership_name)
    if os.environ.get('AWS_SAM_LOCAL') in ['true', 'True', 'TRUE', '1']:
        print('Connecting to local redis')
        rd = redis.Redis(host='host.docker.internal', port=6379) #local only
    else:
        parameters = SSM.get_parameter(Name='/alc/autobots/redis/endpoint')
        remote_endpoint = parameters['Parameter']['Value']
        print('Attempting to connect to AWS Elasticache Redis')
        rd = redis.Redis(host=remote_endpoint, port=6379)

    is_redis_connected = False
    if rd.ping():
        is_redis_connected = rd.ping()
        print('redis connected')  # remove

    dealer_checklist = {}
    if is_redis_connected:
        dealer_checklist = json.loads(rd.get(dealership_name))
        print(dealer_checklist)

    # need to figure out how to handle CORS globally
    response = {
        'statusCode': 200,
        'body': json.dumps({"results": dealer_checklist}),
        'headers': {
            # 'content-type': 'application/json',
            # 'Access-Control-Allow-Methods': 'GET'
            "access-control-allow-origin": "http://localhost:8000"
        }
    }

    return response
