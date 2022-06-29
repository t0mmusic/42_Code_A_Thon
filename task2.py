import os

#converts string to float and multiplies by the multiplier
def	convert_float(factor, multiple):
	return round(float(factor) * multiple, 2)

#Returns the rating the start-up has recieved
def	rating(founder, industry, traction, gut):
	score = founder + industry + traction + gut
	if score >= 4:
			return("P1")
	elif score >= 2.5:
			return("P2")
	elif score >= 1:
			return("P3")
	else:
			return("R")

#Finds the number that do not match the input comparison
def find_number(data, total, index, comp):
	count = 0
	number = total
	while count < total:
		if data[count][index] == comp:
			number -= 1
		count += 1
	return number

#Finds the average across all startups
def find_average(data, total, index):
	count = 0
	average = 0
	while count < total:
		average += float(data[count][index])
		count += 1
	return round(average / total, 2)

#Prints the number of start ups meeting the input criteria, followed by the names of the startups
def	print_list(input_str, current):
	print(input_str, end=": ")
	total = len(current)
	count = 0
	while count < total:
		print(current[count], end="")
		count += 1
		if count < total:
			print(", ", end="")
	print("")
	
#Find the number of startups meeting input criteria and appends all those startups to the list
def number_of(data, total, index, comp):
	lst = []
	lst.append(total - find_number(data, total, index, comp))
	count = 0
	while count < total:
		if data[count][index] == comp:
			lst.append(data[count][0])
		count += 1
	return lst

#Prints all the outputs
def	print_result(data):
	total = len(data)
	print(">>> Number of Start-ups:", total)
	print(">>> Start-up progression rate: " + str(round(find_number(data, total, 9, "R") / total * 100)) + "%")
	print(">>> Average rating for factor 1:", find_average(data, total, 1))
	print(">>> Average rating for factor 2:", find_average(data, total, 2))
	print(">>> Average rating for factor 3:", find_average(data, total, 3))
	print(">>> Average rating for factor 4:", find_average(data, total, 4))
	print_list(">>> Number of P1s", number_of(data, total, 9, "P1"))
	print_list(">>> Number of P2s", number_of(data, total, 9, "P2"))
	print_list(">>> Number of P3s", number_of(data, total, 9, "P3"))
	print_list(">>> Number of Rs", number_of(data, total, 9, "R"))

#Checks that values entered by user are between 0 and 5
def check_bounds(value):
	if float(value) < 0 or float(value) > 5:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("!!! Number entered must be between 0 and 5! !!!")
		return False
	else:
		return True

#Checks that the user has entered a numeric value
def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("!!! Inputs must be numeric! !!!")
		return False

#Defining variables
founder_mult = .3
industry_mult = .3
traction_mult = .35
gut_mult = .05
user_in = ""
data = []

os.system('cls' if os.name == 'nt' else 'clear')
#Loops until user enters "N"
while 1:
	user_in = input("Enter a start-up’s factor rating (separated by comma), type in letter N to finish:\n")
	if user_in == "N":
		#checks if the user has entered any data, and gives them the option to exit
		if len(data) == 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("!!! No startups have been added! !!!")
			user_in = input("If you would like to exit without adding data, type EXIT, otherwise enter anything else: ")
			if user_in == "EXIT":
				quit()
			os.system('cls' if os.name == 'nt' else 'clear')
			continue
		else:
			break
	input_split = user_in.split(",")
	#Checks that user has entered correct number of values
	if len(input_split) != 5:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("!!! You have not entered the correct number of arguments! !!!")
		continue
	#Checks that user has entered numbers
	if (not check_numeric(input_split[1]) 
	or not check_numeric(input_split[2]) 
	or not check_numeric(input_split[3]) 
	or not check_numeric(input_split[4])):
		continue
	if (not check_bounds(input_split[1])
	or not check_bounds(input_split[2]) 
	or not check_bounds(input_split[3]) 
	or not check_bounds(input_split[4])):
		continue
	input_split.append(convert_float(input_split[1], founder_mult))
	input_split.append(convert_float(input_split[2], industry_mult))
	input_split.append(convert_float(input_split[3], traction_mult))
	input_split.append(convert_float(input_split[4], gut_mult))
	input_split.append(rating(input_split[5], input_split[6], input_split[7], input_split[8]))
	data.append(input_split)
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Added successfully!")
#prints results
print_result(data)
#output results into a file for use in task3
import csv
output_file = open('data.csv', 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(data)
output_file.close()