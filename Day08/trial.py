marks = [45, 78, 92, 34, 67, 88, 55]
total = sum(marks)
print("Total marks:", total)
avg = total/len(marks)
print("Average marks:", avg)
high = max(marks)
low = min(marks)
print("highest marks:", high)
print("Lowest marks:",low)
passed = 0
fail = 0

for mark in marks:
  if mark>avg:
    print(mark)
  if mark>=40:
    passed += 1
  else:
    fail += 1
print("Passed:", passed)
print("Failed:", fail)

even=0
odd=0

for mark in marks:
  if mark%2 == 0:
    even += 1
   
  else:
    odd += 1

print("Even no.:", even)
print("Odd no.:", odd)



sorted_marks = sorted(marks, reverse=True)

print("The second highest mark:",sorted_marks[1])

for mark in marks:
  if mark>avg:
    print(mark)

  