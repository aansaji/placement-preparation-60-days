import numpy as np
marks = np.array([
    [45, 67, 82],
    [91, 56, 74],
    [88, 79, 93]
])

print(marks[1])
print(marks[:,0])
print(marks[marks>80])
print("Average:", marks.mean())
