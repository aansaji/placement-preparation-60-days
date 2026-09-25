file = open("data.txt","w")
file.write("Python is easy")
file.close()
file = open("data.txt", "r")
print(file.read())
file.close()

with open("students.txt", "w") as file:
    file.write("Aan\nRahul\nAnu")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())