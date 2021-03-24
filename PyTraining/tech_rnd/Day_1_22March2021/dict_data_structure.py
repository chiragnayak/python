print('-' * 75)

# Dictionary => Collection of key value pairs
# key should be unique within the dictionary, as these keys will act as indexes
# Any immutable type can be given as a key
# values can be of any type and it can be repeated
# Enclosed in {}
# Unordered Collection

# Dictionary
emp = {
    'name': 'davies',
    'loc': 'blr',
    'sal': 15000,
    'name': 'justin'
}
print(emp, '-', type(emp))
print('Name -', emp['name'])
print('Name using GET -', emp.get('name'))

# print('Team -', emp['team'])             # throws KeyError
print('Team using GET -', emp.get('team', 'testing'))
print('emp -', emp)

print('-' * 75)

# Use of Membership Operator => Checks for the existence of keys in dictionary
print('Is team present in emp -', 'team' in emp)

print('-' * 75)

# Add/Modify the key-value pair
emp['sal'] = 25000
emp['team'] = 'support'
print('After Add/Modify -', emp)

print('-' * 75)

# emp_details
emp_details = {
    'sal': 35000,
    'project': 'telecom',
    'mgr': 'damien'
}

# Update method
# It will modify the key-value pair, if the key already exists
# It will add the key-value pair, if the key does not exists
emp.update(emp_details)
print('After update -', emp)

print('-' * 75)

# pop => delete the key-value pair
removed = emp.pop('loc')
print('Value Removed -', removed)
print('After Pop -', emp)

# del
del emp['sal'], emp['project']
print('After Del -', emp)

print('-' * 75)

# Iterating through the dictionary object
print('emp -', list(emp))
for key in emp:
    print(key, '-', emp[key])

print('-' * 75)

# Iterating through the keys() method
print('emp -', emp.keys())
for key in emp.keys():
    print(key, '-', emp[key])

print('-' * 75)

# Iterating through the values() method
print('emp -', emp.values())
for value in emp.values():
    print(value)

print('-' * 75)

# Iterating through the key-value pairs using items() method
print('emp -', emp.items())
for key, value in emp.items():
    print(key, '-', value)

print('-' * 75)

# Clear all the key-value pairs
emp.clear()
print('After Clear -', emp)

print('-' * 75)
