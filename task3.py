import csv
import os

from os.path import exists

#Checks if a file has been generated containing user data
file_exists = exists("data.csv")
if file_exists == False:
	print("No user data exists!")
	quit()

#opens the csv file containing the data from task 2 and saves it to a list
with open("data.csv",'r') as custfile:
	reader = csv.reader(custfile,delimiter=',')
	data = list(reader)

total = len(data)

#Shows all startups of the input type. If there are none, prints a seperate message
def present_all(in_type):
	os.system('cls' if os.name == 'nt' else 'clear')
	count = 0
	flag = False
	while count < total:
		if data[count][9] == in_type:
			flag = True
			print(data[count][0])
		count += 1
	if flag == False:
		print(">>> No startup satisfied requirement for " + in_type + " ratings.")

#Checks that value entered by the user is positive
def check_bounds(value):
	if float(value) < 1:
		return False
	else:
		return True

#Checks that the user has entered a numeric value
def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		print("Inputs must be numeric!")
		return False

#Returns the score the start-up has recieved
def	score(founder, industry, traction, gut):
	score = float(founder) + float(industry) + float(traction) + float(gut)
	return score

#Creates a list of all the scores
def	find_scores():
	ratings = []
	count = 0
	while count < total:
		ratings.append(score(data[count][5],
			data[count][6],
			data[count][7],
			data[count][8]))
		count += 1
	return ratings

#Returns the index of the largest value in the list, making that number 0
def find_largest(ratings):
	maximum = max(ratings)
	if maximum < 1:
		return -1
	else:
		ret = ratings.index(maximum)
		ratings[ret] = 0
		return ret

#Prompts user to enter the number of businesses to invest in
def	business_number():
	user_in = input(">>> How many businesses do you want to invest in:")
	os.system('cls' if os.name == 'nt' else 'clear')
	if not check_numeric(user_in):
		print("Please enter a numeric value.")
		return
	if not check_bounds(user_in):
		print("Number must be a positive value.")
		return
	bus_num = int(user_in)
	count = 0
	flag = False
	ratings = find_scores()
	while count < bus_num:
		count += 1
		index = find_largest(ratings)
		if index >= 0:
			print(data[index][0] + ", " + data[index][9])
			flag = True
		elif flag == True and count != bus_num:
			print("No more companies meet the criteria.")
			return
	if flag == False:
		print("There are no companies worth investing in :(")

#Prompts the user to enter one of the options
os.system('cls' if os.name == 'nt' else 'clear')
while 1:
	print("1. Present all P1")
	print("2. Present all P2")
	print("3. Present all P3")
	print("4. Present all R")
	print("5. How many businesses do you want to invest in")
	print("6. Terminate")
	user_in = input("Which option do you want to see: ")
	if user_in == "1":
		present_all("P1")
	elif user_in == "2":
		present_all("P2")
	elif user_in == "3":
		present_all("P3")
	elif user_in == "4":
		present_all("R")
	elif user_in == "5":
		business_number()
	elif user_in == "6":
		quit()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Invalid option!")