def	convert_float(factor, multiple):
	return float(factor) * multiple

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

def find_number(data, total, index, comp):
	count = 0
	number = total
	while count < total:
		if data[count][index] == comp:
			number -= 1
		count += 1
	return number

def find_average(data, total, index):
	count = 0
	average = 0
	while count < total:
		average += data[count][index]
		count += 1
	return round(average / total, 2)

def	print_result(data):
	total = len(data)
	print("Number of Start-ups:", total) #Number of companies
	print("Start-up progression rate:", round(find_number(data, total, 9, "R") / total * 100, 0), "%") #number that passed
	print("Average rating for factor 1:", find_average(data, total, 5))
	print("Average rating for factor 2:", find_average(data, total, 6))
	print("Average rating for factor 3:", find_average(data, total, 7))
	print("Average rating for factor 4:", find_average(data, total, 8))

def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		print("Inputs must be numeric!")
		return False

founder_mult = .3
industry_mult = .3
traction_mult = .35
guts_mult = .05
user_in = ""
data = []
while 1:
	user_in = input("Enter a Start-up’s factor ratings (separated by comma):")
	if user_in == "N":
		break
	input_split = user_in.split(",")
	if len(input_split) != 5:
		print("You have not entered the correct number of arguments!")
		continue
	if not check_numeric(input_split[1]) or not check_numeric(input_split[2]) or not check_numeric(input_split[3]) or not check_numeric(input_split[4]):
		continue
	input_split.append(convert_float(input_split[1], founder_mult))
	input_split.append(convert_float(input_split[2], industry_mult))
	input_split.append(convert_float(input_split[3], traction_mult))
	input_split.append(convert_float(input_split[4], guts_mult))
	input_split.append(rating(input_split[5], input_split[6], input_split[7], input_split[8]))
	data.append(input_split)

print(data)
print_result(data)