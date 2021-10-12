import json
# from redis_connection import get_redis_connection
# import ptvsd
import os
import redis
# import boto3
#
# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()


# SSM = boto3.client('ssm', region_name=os.environ.get('AWS_REGION'))
# parameters = SSM.get_parameter(Name='/alc/autobots/redis/endpoint', Region=os.environ.get('AWS_REGION'))
# remote_endpoint = parameters['Parameter']['Value']


def lambda_handler(event, context):
    print('\n*** Dealer updating checklist...')
    conn = None
    print('EVENT', event)
    if os.environ.get('AWS_SAM_LOCAL') in ['true', 'True', 'TRUE', '1']:
        conn = redis.Redis(host='host.docker.internal', port=6379)  # local only
    # else:
    #     conn = redis.Redis(host=remote_endpoint, port=6379)

    body = event['body']
    print('Update Request Body', body)

    dealership_name = event['pathParameters']['dealershipName']
    print(f'updating checklist for dealer: {dealership_name}')

    is_complete = False
    if body and type(body) == 'dict':
        is_complete = all(body.values())
    print('is_complete', is_complete)

    if conn.ping:
        print(f'Updating checklist in Redis for dealer: {dealership_name}')
        conn.set(dealership_name, body)

    return {
        'statusCode': 200,
        'headers': { 
            'access-control-allow-origin': 'http://localhost:8000'
        },
        'body': json.dumps({
            'id': dealership_name,
            'isComplete': is_complete
        })
    }