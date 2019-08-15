import requests
import json

url = 'http://202.207.12.223:8000/step_04'

response = requests.get(url)

question = json.loads(response.text)

array = eval(question["questions"])
print(array)

ans = ''
array_length = len(array)
array_length_num = len(array[0])


def ksm(x):
    num = 1
    a = x[0]
    b = x[1]
    mode = x[2]
    a = a % mode
    while b != 0:
        if b & 1:
            num = (num * a) % mode
        b >>= 1
        a = (a * a) % mode
    return num


print(ksm(array[0]))
for i in range(0, 10):
    result = str(ksm(array[i]))
    ans += result
    if i != 9:
        ans += ','

print(ans)

get_url = '?ans=' + ans
url = url + get_url
print(url)
response_ans = requests.get(url)
print(response_ans.text)
