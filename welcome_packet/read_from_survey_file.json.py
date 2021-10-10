import json
from operator import itemgetter


def lambda_handler(event, context):
    with open('./WO-092221-001/WO-092221-001-SurveyForm.json', mode='r') as f:
        content = json.load(f)

    dealershipname, userdetails, endcustomerinfo = itemgetter('dealershipname', 'userdetails', 'endcustomerinfo')(
        content)
    return {
        'statusCode': 200,
        "body": {
            "message": "hello world",
            "dealership": dealershipname,
            "userdetails": userdetails,
            "endcustomerinfo": endcustomerinfo
            # "location": ip.text.replace("\n", "")
        },
    }


response = lambda_handler(None, None)
json_str = json.dumps(response, indent=2)
py_dict = json.loads((json_str))

print('----------------------')
print(type(json_str))
print(json_str)

# TypeError: string indices must be integers
# print(json_str['endcustomerinfo']) <- cannot do this
# print(json_str(['body']['endcustomerinfo']))


print('----------------------')
print(type(py_dict))
print(py_dict)


body = py_dict['body']
print('-----dealership --------')
print(body['dealership'])

print('---- userdetails -----')
print(body['userdetails'])

print('----- endcustomerinfo -----')
print(body['endcustomerinfo'])