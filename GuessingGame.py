#-------------------------------------------------------------------------
# Name:		    Lesson 5.7 Break & Continue
# Purpose:		Guessing Game with Break
# Author:		  
# Created:		06/05/2024
#-------------------------------------------------------------------------

import random

num = random.randrange(1, 101)

while True:
  guess = int(input("Enter a guess: "))

  if guess == num:
    break
  elif guess > num:
    print("Guess is too high. Guess again.")
  elif guess < num:
    print("Guess is too low. Guess again.")

print("Congratulations! You guessed correct!")