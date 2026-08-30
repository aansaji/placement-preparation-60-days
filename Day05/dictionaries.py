students = [
    {"name": "Aan", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Anjali", "marks": 91},
    {"name": "John", "marks": 35}
]

passed = 0
for student in students:
  print(student["name"], student["marks"])
  if student["marks"] >=40:
    print("passed")