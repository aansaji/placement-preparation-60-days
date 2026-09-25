try:
   x = int(input("enter a number:"))
   result = (100/x)
except ValueError:
   print("Enter number")
except ZeroDivisionError:
   print("Cannot divide by zero")
else:
   print(int(result ))
finally:
   print("Program has finished")

