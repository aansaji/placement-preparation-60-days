print("====== STUDENT MANAGEMENT SYSTEM ======")

name = input("\nEnter student name:")
maths = int(input("Enter the marks for maths: "))
science = int(input("Enter the marks for science: "))
english = int(input("Enter the marks for english : "))
comp = int(input("Enter the marks for computer : "))
hindi = int(input("Enter the marks for hindi: "))

total = (maths+science+english+comp+hindi)
average = (maths+science+english+comp+hindi)/5

print("Total Marks: ", total)
print("Average Marks: ", average)

if average >= 90:
  print("Grade A")
elif average >= 80:
  print("Grade B")
elif average >= 65:
  print("Grade C")
else:
  print("Grade D")


if average >= 65:
  print("Pass")
else:
  print("Fail")

print("====================================")