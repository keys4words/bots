import requests
from pprint import pprint

response = requests.get('https://stepik.org/api/search-results',
                        params={'query': 'python',
                                'is_popular': False })
# print(response.json()['courses'][0]['id'])
titles = []
for course in response.json()['search-results']:
    titles.append(course['course_title'])

pprint(titles)