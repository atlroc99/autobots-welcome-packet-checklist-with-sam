import redis
import json
import boto3
import os
# import ptvsd

# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()

current_region = os.environ.get('AWS_REGION')
SSM = boto3.client('ssm', region_name=current_region)


def lambda_handler(event, context):
    print('\n*** Dealer Submitting form...')

    print('EVENT: ', event)
    body = event.get('body')
    dealership_name = event['pathParameters']['dealershipName']
    print('SUBMIT FORM REQUEST BODY', body)

    rd = None
    if os.environ.get('AWS_SAM_LOCAL') in ['true', 'True', 'TRUE', '1']:
        print('connecting to local redis')
        rd = redis.Redis(host='host.docker.internal', port=6379)
    else:
        print('connecting to remote redis')
        parameter = SSM.get_parameter(Name='/alc/autobots/redis/endpoint')
        endpoint = parameter['Parameter']['Value']
        redis.Redis(host=endpoint, port=6379)
        print('connected to remote redis')

    is_connected = False
    if rd and rd.ping():
        is_connected = True

    if is_connected:
        print(f'Submitting checklist for dealership_name: {dealership_name}')
        rd.set(dealership_name, body)

    response_body = {
        'id': dealership_name
    }

    return {
        'statusCode': 200,
        'headers': {
           'access-control-allow-origin': 'http://localhost:8000'
        },
        'body': json.dumps(response_body)
    }
