import os

#global variables for multipliers (for easy modification!)
founder_mult = .3
industry_mult = .3
traction_mult = .35
gut_mult = .05

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

#class declaration for Startup objects. Contains 10 variables which are initialised on creation
class Startup:
	def __init__(self, name, founder, industry, traction, gut):
		#sets the variables input by user
		self.name = name
		self.founder = round(float(founder), 2)
		self.industry = round(float(industry), 2)
		self.traction = round(float(traction), 2)
		self.gut = round(float(gut), 2)
		#sets the variables that need conversion
		self.fou_score = self.founder * founder_mult
		self.ind_score = self.industry * industry_mult
		self.tra_score = self.traction * traction_mult
		self.gut_score = self.traction * gut_mult
		#sets the rating for the startup
		self.rating = rating(self.fou_score,
							self.ind_score,
							self.tra_score,
							self.gut_score)

#Finds the percentage of startups that meet a rating condition
def find_percent(data, total, comp):
	number = total
	for x in data:
		if x.rating == comp:
			number -= 1
	return str(round(number / total * 100)) + "%"

#Finds the average across all startups
def find_average(data, total, match):
	average = 0
	for x in data:
			average += getattr(x, match)
	return round(average / total, 2)
	
#Find the number of startups meeting input criteria and appends all those startups to the list
def number_of(data, comp):
	count = 0
	for x in data:
		if x.rating == comp:
			count += 1
	return count

#Prints all the outputs
def	print_result(data):
	total = len(data)
	print(">>> Number of Start-ups:", total)
	print(">>> Start-up progression rate: " + find_percent(data, total, "R"))
	print(">>> Average rating for factor 1:", find_average(data, total, "founder"))
	print(">>> Average rating for factor 2:", find_average(data, total, "industry"))
	print(">>> Average rating for factor 3:", find_average(data, total, "traction"))
	print(">>> Average rating for factor 4:", find_average(data, total, "gut"))
	print(">>> Number of P1s:", number_of(data, "P1"))
	print(">>> Number of P2s:", number_of(data, "P2"))
	print(">>> Number of P3s:", number_of(data, "P3"))
	print(">>> Number of Rs:", number_of(data, "R"))

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
user_in = ""
data = []

os.system('cls' if os.name == 'nt' else 'clear')
#Loops until user enters "N"
while 1:
	try:
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
		new_startup = Startup(input_split[0],
								input_split[1],
								input_split[2],
								input_split[3],
								input_split[4]) 
		data.append(new_startup)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Added successfully!")
	except KeyboardInterrupt:
		print("Exiting Programming.")
		quit()
#prints results
print_result(data)
#output results into a file for use in task3
import csv
output_file = open('data.csv', 'w')
datawriter = csv.writer(output_file)
output_data = []
for x in data:
	out_list = []
	out_list.append(x.name)
	out_list.append(x.founder)
	out_list.append(x.industry)
	out_list.append(x.traction)
	out_list.append(x.gut)
	out_list.append(x.fou_score)
	out_list.append(x.ind_score)
	out_list.append(x.tra_score)
	out_list.append(x.gut_score)
	out_list.append(x.rating)
	output_data.append(out_list)
datawriter.writerows(output_data)
output_file.close()