print('-' * 75)

import json

# Dictionary
emp = {
    1: {
        'name': 'justin',
        'loc': 'kochin'
    },
    2: {
        'name': 'tris',
        'loc': 'hyderabad'
    },
    3: {
        'name': 'davies',
        'loc': 'noida'
    }
}
print(emp, '-', type(emp))

print('-' * 75)

# Convert dictionary to JSON object
json_obj = json.dumps(emp)
print(json_obj, '-', type(json_obj))

print('-' * 75)

# Convert JSON object to Python Native Datatype
json_dict = json.loads(json_obj)
print(json_dict, '-', type(json_dict))

# Parse the content
print('Only 3rd Record -', json_dict['3'])
print('Name from 3rd Record -', json_dict['3']['name'])

print('-' * 75)

# Write the dictionary to JSON file
with open(r'files/data.json', 'w') as json_write:
    json.dump(emp, json_write, indent=4)
print('JSON File Written')

print('-' * 75)

# Read the content of JSON in the form of Python Datatype
with open(r'files/data.json') as json_read:
    json_dict = json.load(json_read)
print(json_dict, '-', type(json_dict))

print('-' * 75)

emp = {
    "count": 1,
    "alerts": [
        {
            "nsxtManager": "10.79.65.233",
            "eventTags": [
                "NSX-T"
            ],
            "displayName": "Routing Advertisement disabled",
            "name": "NSXTRoutingAdvertisementEvent",
            "eventSeverity": "Warning",
            "eventType": "Problem",
            "intentName": "",
            "manager": "10.79.65.233",
            "anchorEntities": [
                "oc-cl1-kube-public"
            ],
            "recommendations": [
                "Enable route advertisement on Tier-1 logical router."
            ],
            "reason": "",
            "message": "Routing advertisement for Tier-1 logical router oc-cl1-kube-public is disabled",
            "definedBy": "System",
            "description": [
                "Routing advertisement is disabled for NSX-T Tier-1 logical router. Networks under this router are not reachable from outside."
            ]
        }
    ]
}

res_json = json.dumps(emp) #default=lambda o: o.__dict__)
print(res_json)

print('-' * 75)
