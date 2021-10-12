import json

resp = {
    'isYellow': True,
    'isGreen': True,
    'isRed': True
}

# get values of object
print(type(resp.values()))
print(all(resp.values()))

print(f"using in : {False in resp.values()}")

# is_complete = True
# for k,v in resp.items():
#     if v == False:
#         print('not completed')
#         is_complete = False
#         break
#
# print(f'is_complete: {is_complete}')

with open('../checklists/minified_checklist.json', mode='r') as from_checklist_file:
    checklists = json.load(from_checklist_file)

items = checklists.get('checklist')
system_name = 'webCTRL'
for item in items:
    item['label'] = item['label'].replace('{systemName}', system_name)

print(checklists)


with open('../../events/event.json', mode='r') as event_file:
    event = json.load(event_file)

# print(event)
dealer_name = event['pathParameters']['dealershipName']
print(dealer_name)

