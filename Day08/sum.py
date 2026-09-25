numbers = [12, 7, 25, 18, 30, 11, 40]
even = 0
for n in numbers:
  if n%2==0:
    even += n
print(even)


odd = 0
for n in numbers:
  if n%2!=0:
    odd += n
print(odd)

