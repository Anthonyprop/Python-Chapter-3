"""
Program: random_guess.py
Author: Pierre
Date: 09/05/2019

program asks the user for a high and low

"""
import random

# Accept the input
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# Program will generate a random number in that range
myNumber = random.randint(smaller, larger)

# Accumulator to keep track of how many tries the user makes
count = 0

# Loop which contains the game mechanics
while True:
	count += 1
	userNumber = int(input("Enter your guess: "))
	if userNumber < myNumber:
		print("Too small!")
	elif userNumber > myNumber:
		print("Too large!")
	else:
		print("Congrats! You got it in", count, "tries!")
		break

print("Thank you for playing!")