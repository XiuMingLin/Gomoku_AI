import json
import requests

url = 'http://202.207.12.223:8000/step_02'  # ?name=Aqua&student_number=0171123396'

data = {
    'name': 'Aqua',
    'student_number': '0171123396'
}

get_url = '?name=' + data['name'] + '&student_number=' + data['student_number']
url = url + get_url
print(url)

response = requests.get(url)
# print(response.url)
print(response.text)


