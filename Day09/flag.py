numbers = [12, 7, 25, 18, 30, 11, 40, 50]
odd=0
even=0

found=False
for n in numbers:
  if n%2==0:
    print("Even no.:", n)
    even += 1
  else:
    print("Odd no.:", n)
    odd +=1

print("Even count:", even)
print("Odd Count:", odd)

sorted_num = sorted(numbers)
print("The largest no.:", sorted_num[-1])
print("The second largest no.:", sorted_num[-2])

for n in numbers:
  if n==30:
    found=True
    break
if found:
  print("Found")
else:
  print("Not found")
