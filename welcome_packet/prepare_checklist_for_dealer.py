'''
    read form checklist file and create a checklist json object and return
'''
import json


def lambda_handler(event, context):
    with open('./checklists/minified_checklist.json') as from_checklist_file:
        checklist = json.load(from_checklist_file)
    # print(type(checklist))
    # print_pretty_json(checklist)
    response_body = {
        'statusCode': 200,
        'headers': {
            'content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({'results' : checklist})
    }
    print('response_body:',response_body)
    return response_body

# def print_pretty_dict_json(data: dict):
#     print(f'the type is: {type(data)}')
#     print(json.dumps(data, indent=2))
#
# def print_pretty_string_json(data: str):
#     print(json.dumps(data, indent=2))
#
#
# resp = lambda_handler(None, None)
# print_pretty_dict_json(resp)
