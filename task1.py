from decimal import *

#Prints the rating the start-up has recieved
def	rating(founder, industry, traction, gut):
	score = round(founder + industry + traction + gut, 0)
	if score >= 4:
			print("P1")
	elif score >= 2.5:
			print("P2")
	elif score >= 1:
			print("P3")
	else:
			print("R")

#Converts string to float and multiplies by the multiplier
def	convert_float(factor, multiple):
	return Decimal(factor) * Decimal(multiple)

#Checks that the user has entered a numeric value
def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		print("Inputs must be numeric!")
		return False

#Defining variables
founder_mult = ".3"
industry_mult = ".3"
traction_mult = ".35"
gut_mult = ".05"

user_in = input("Enter a Start-up’s factor ratings (separated by comma):")
input_split = user_in.split(",")
if len(input_split) != 5:
		print("You have not entered the correct number of arguments!")
		quit()
if (not check_numeric(input_split[1]) 
	or not check_numeric(input_split[2]) 
	or not check_numeric(input_split[3]) 
	or not check_numeric(input_split[4])):
		quit()
rating(convert_float(input_split[1], founder_mult), 
		convert_float(input_split[2], industry_mult),
		convert_float(input_split[3], traction_mult),
		convert_float(input_split[4], gut_mult))