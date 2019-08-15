import requests
import json

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


def addkey(x):
    return x[0] * (x[1] ** x[2])


url = 'http://202.207.12.223:8000/step_05'

key = [65537,
135261828916791946705313569652794581721330948863485438876915508683244111694485850733278569559191167660149469895899348939039437830613284874764820878002628686548956779897196112828969255650312573935871059275664474562666268163936821302832645284397530568872432109324825205567091066297960733513602409443790146687029]

# num = [31415926]
#
#
# num = num + key
# num = ksm(num)
# print(num)
#
# get_url = '?num=' + str(num)
# url = url + get_url
# response = requests.get(url)
# print(response.text)

key_str = '123321'
key_str_len = len(key_str)
# print(key_str_len)

str2num = 0

for i in range(0, key_str_len):
    array = [ord(key_str[i]), 256, key_str_len - 1 - i]
    # print(array)
    str2num += addkey(array)

# print(str2num)
# str2num = url + '?str2num=' + str(str2num)
# print(str2num)
# response = requests.get(str2num)
# print(response.text)

str2num = [str2num] + key
str2num = ksm(str2num)

# str2num = url + '?str=' + str(str2num)
# response = requests.get(str2num)
# print(response.text)

hex_str2num = hex(str2num)
# hex_str2num = url + '?hex=' + str(hex_str2num)
# response = requests.get(hex_str2num)
# print(response.text)

total_url = url + '?user=' + 'aqua' + '&password=' + hex_str2num
print(total_url)
response = requests.get(total_url)
print(response.text)
other_ppn = json.loads(response.text)
other_ppn = other_ppn['message']

other_ppn = int(other_ppn, 16)
print(other_ppn)
# 72443802841723883314398378489118083178294116707448787916389537797675865876581801631378782024312409859062441624125400361559594135432625891794531243436494273942144660211246847356735716961511255372488979752643679406560991098240459652871545991629229693900782962762922945163077997561230543946531285122001109004763

share_key = ksm([other_ppn, key[0], key[1]])
print(share_key)

def int_to_asmii(x):
    ascii_str = ''
    while x > 0:
        ascii_str = chr(x % 256) + ascii_str
        x = x // 256
    return ascii_str

share_key = int_to_asmii(share_key)
print(share_key)
