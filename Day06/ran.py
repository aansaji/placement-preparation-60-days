import random
num = random.randint(1,10)  
guess = int(input("Guess the number between 1-10:"))
if guess == num:
  print("Correct")
else:
  print("You guessed wrong")
  print("The number is:", num)