import json


with open('channel_users.json', 'r', encoding='utf8') as f:
    persons = json.load(f)

print(len(persons))