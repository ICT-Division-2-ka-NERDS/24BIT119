# 24bit119

# Que-7

import json
from datetime import datetime

employee = {
    "empcode": 103,
    "empname": "Charlie Brown",
    "date_of_joining": "2022-08-01",
    "salary": 90000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
print("Employee data saved to employee.json")

with open("employee.json", "r") as file:
    loaded_employee = json.load(file)

print("Employee data loaded from file:")
print(loaded_employee)
