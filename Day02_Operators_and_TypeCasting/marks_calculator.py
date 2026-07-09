print("========= STUDENT REPORT =========")
name = input("Name: ")
m = int(input("Math: "))
s = int(input("Science: "))
e = int(input("English: "))
p = int(input("Physics: "))
c = int(input("Chemistry: "))

total = (m+s+e+p+c)
avg = (total/5)

print("\n\nTotal: ", total) 
print("Average: ", avg)
if avg >= 40:
  print("Passed: True")
else:
  print("Failed")
print("==================================")





print("========= STUDENT REPORT =========")
name = input("Name: ")
m = int(input("Math: "))
s = int(input("Science: "))
e = int(input("English: "))
p = int(input("Physics: "))
c = int(input("Chemistry: "))

total = (m+s+e+p+c)
avg = (total/5)

print("\n\nTotal: ", total) 
print("Average: ", avg)
if avg >= 90:
  print("Passed: True \nGrade A")
elif avg >= 80 :
  print("Passed: True \nGrade B")
elif avg >=70:
  print("Passed: True \nGrade C")
elif avg >= 60:
  print("Passed: True \nGrade D")
else:
  print("Passed: True \nGrade F")
  
print("==================================")

