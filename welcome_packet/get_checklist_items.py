import json
from operator import itemgetter

# import requests


def lambda_handler(event, context):
    with open('minified_checklist.json', mode='r') as f:
        data = json.load(f)

    # print(data['checklist'][0])
    item = data['checklist'][0]
    name, isChecked, label = itemgetter('name', 'isChecked', 'label')(item)
    # print(f'name: {name} | isChecked: {isChecked} | label: {label}')
    return {
        "statusCode": 200,
        "body": {
            "message": "hello world",
            "name": name,
            "isChecked": isChecked,
            "label": label
            # "location": ip.text.replace("\n", "")
        },
    }

response = lambda_handler(None, None)
print(json.dumps(response,indent=2))
