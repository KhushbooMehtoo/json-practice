import json

employees = [
    {
        "id": 1,
        "name": "Khushboo",
        "phone": "8907478464",
        "email": ["khush@gmail.com", "khushbu12@gmail.com"],
        "present": True
    },
    {
        "id": 2,
        "name": "Atul",
        "phone": "5656576767",
        "email": None,
        "present": True
    }
]
with open("employe_json.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Data successfully saved")


# ---------------- READ----------------


with open( "employe_json.json","r") as file:
    emp = json.load(file)
print(emp)

# ---------------- CREATE (ADD) ----------------
new_emp={
    "id":3,
    "name":"Khushi",
    "phone":"8484848884",
    "email":["khuhsi@gmail.com",None],
    "present":False
}

emp.append(new_emp)

with open("employe_json.json","w")as file:
    json.dump(emp,file,indent=4)

print("Employee added successfully")


# ---------------- UPDATE ----------------

for e in emp:
    if e["email"]==None:
        e["email"]=["abc@gmail.com","xyz@gmail.com"]

with open("employe_json.json","w")as file:
    json.dump(emp,file,indent=4)

print("Update successfully")

# ---------------- DELETE (KEY DELETE) ----------------

for e in emp:
    if "present" in e:
        del e["present"]

with open("employe_json.json","w")as f:
    json.dump(emp,f,indent=4)
    

print("present key deleted")