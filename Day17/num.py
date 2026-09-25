import numpy as np

marks = np.array([45, 67, 82, 91, 56, 74])

print("Total:",marks.sum())
print("Average:",marks.mean())
print("Highest:", marks.max())
print("lowest:", marks.min())
print(marks*2)
print(marks[2])
print(marks[-2:])
print(marks[1:4])
print(marks[marks>60])
print(marks[(marks>50)&(marks<90)])
marks[marks<60]=60
print (marks)
print(marks+5)

