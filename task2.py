#converts string to float and multiplies by the multiplier
def	convert_float(factor, multiple):
	return float(factor) * multiple

#Returns the rating the start-up has recieved
def	rating(founder, industry, traction, guts):
	score = founder + industry + traction + guts
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
def	print_list(current, input_str):
	print(input_str, end=": ")
	total = len(current)
	count = 0
	while count < total:
		print(current[count], end="")
		count += 1
		if count < total:
			print(",", end="")
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
	print("Number of Start-ups:", total)
	print("Start-up progression rate:", round(find_number(data, total, 9, "R") / total * 100, 0), "%")
	print("Average rating for factor 1:", find_average(data, total, 1))
	print("Average rating for factor 2:", find_average(data, total, 2))
	print("Average rating for factor 3:", find_average(data, total, 3))
	print("Average rating for factor 4:", find_average(data, total, 4))
	print_list(number_of(data, total, 9, "P1") , "Number of P1s")
	print_list(number_of(data, total, 9, "P2") , "Number of P2s")
	print_list(number_of(data, total, 9, "P3") , "Number of P3s")
	print_list(number_of(data, total, 9, "R") , "Number of Rs")

#Checks that the user has entered a numeric value
def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		print("Inputs must be numeric!")
		return False

#Defining variables
founder_mult = .3
industry_mult = .3
traction_mult = .35
guts_mult = .05
user_in = ""
data = []

#Loops until user enters "N"
while 1:
	user_in = input("Enter a start-up’s factor rating (separated by comma), type in letter N to finish:\n")
	if user_in == "N":
		break
	input_split = user_in.split(",")
	#Checks that user has entered correct number of values
	if len(input_split) != 5:
		print("You have not entered the correct number of arguments!")
		continue
	#Checks that user has entered numbers
	if (not check_numeric(input_split[1]) 
	or not check_numeric(input_split[2]) 
	or not check_numeric(input_split[3]) 
	or not check_numeric(input_split[4])):
		continue
	input_split.append(convert_float(input_split[1], founder_mult))
	input_split.append(convert_float(input_split[2], industry_mult))
	input_split.append(convert_float(input_split[3], traction_mult))
	input_split.append(convert_float(input_split[4], guts_mult))
	input_split.append(rating(input_split[5], input_split[6], input_split[7], input_split[8]))
	data.append(input_split)
#prints results
print_result(data)