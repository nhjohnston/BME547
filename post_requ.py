import requests

out_data = {
    "Name": "nhj4",
    "Match": "No"
}
get = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nhj4")
answer = get.json()
print(answer)
get_type_M1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1")
get_type_F6 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
type_M1 = get_type_M1.text
type_F6= get_type_F6.text
print(type_M1, type_F6)
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json = out_data)
check = r.text
print(check)