import urllib.request
f = urllib.request.urlopen('http://202.207.12.223:8000/step_01')
print(f.read())
