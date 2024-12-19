import requests
people_in_space =requests.get('http://api.open-notify.org/astros.json')
people_in_space_json =people_in_space.json()
#print(people_in_space_json)
#print('The people currently in space are: ')
for person in people_in_space_json['people']:
    print(person['craft'])
