marks = [45, 78, 92, 34, 67, 88]

total=0
passed=0
failed = 0

for mark in marks:
  total += mark
  if mark >= 40:
    passed += 1
  else:
    failed +=1
   

High = max(marks)
Low = min(marks)
average = (total/ len(marks))
print("Highest Marks:", High)
print("Lowest Marks:", Low)
print("Total:", total)
print("Average:", average)
print("Passed:", passed)
print("Failed:", failed)