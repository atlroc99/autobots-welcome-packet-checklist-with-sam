'''
    read form checklist file and create a checklist json object and return
'''
import json


def lambda_handler(event, context):
    print('\n*** Preparing checklist for Dealer ...readin from file')
    with open('./checklists/minified_checklist.json') as from_checklist_file:
        from_file = json.load(from_checklist_file)
    # print(type(checklist))
    # print_pretty_json(checklist)
    # check with Shannon
    system_name = 'i-Vu'
    items = from_file.get('checklist')
    for item in items:
        item['label'] = item['label'].replace('{systemName}', system_name)

    print('from_file', from_file)
    response_body = {
        'statusCode': 200,
        'body': json.dumps({'results': from_file}),
         'headers': {
            'Access-Control-Allow-Origin': 'http://localhost:8000',
        },
    }
    print('response_body:',response_body)
    return response_body
