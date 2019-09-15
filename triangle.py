"""
Program: triangle.py
Author: Pierre
Date: 09/05/2019

Program asked user to accept the lengths of three sides 
of trigle as input. It should output whether or not 
the triangle is an equilateral triangle.

"""

# Request the inputs
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

# Determine if all sides are equal
if side1 == side2 and side2 == side3:
	print("We have an equal triangle!")
else:
	print("Not an equilateral triangle")
