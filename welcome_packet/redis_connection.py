import json
import redis
import os
import boto3
# from operator import itemgetter
# use of itemgetter: a,b = itemgetter(a,b)(py-dict)

SSM = boto3.client('ssm')
parameters = SSM.get_parameter(Name='/alc/autobots/redis/endpoint', Region=os.environ.get('AWS_REGION'))
remote_endpoint = parameters['Parameter']['Value']


def get_redis_connection(event, context):
    print('getting redis connection')
    # print('EVENT', event)
    # TRIED rd = redis.Redis(host='docker.for.mac.localhost', port=6379)
    conn = None
    dealership_name = event['pathParameters']['dealershipname']
    if 'False' in os.environ.get('AWS_SAM_LOCAL'):
        conn = redis.Redis(host='host.docker.internal', port=6379) #local only
    else:
        conn = redis.Redis(host=remote_endpoint, port=6379)
    return conn


