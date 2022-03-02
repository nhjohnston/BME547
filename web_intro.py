import requests


r = requests.get("http://api.github.com/repos/nhjohnston/BME547/branches")
print(r)
print(type(r))
print("Status code = {}".format(r.status_code))
print("Text = {}".format(r.text))
answer = r.json()


for branch in answer:
    print(branch["name"])
print("Done")
