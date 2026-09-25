text = "Programming is Amazing"

print("\n",len(text),"\n")
print(text.upper(),"\n")
print(text.lower(),"\n")
print(text.split(),"\n")

count = 0

for char in text:
  print(char)

for char in text:
 if char.lower() in "aeiou":
    count += 1
print("\nVowels:",count)
  