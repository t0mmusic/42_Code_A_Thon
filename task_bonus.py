#global variables for multipliers (for easy modification!)
founder_mult = .3
industry_mult = .3
traction_mult = .35
gut_mult = .05

#global list of all start-up objects
data = []

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

#Checks that the user has entered a numeric value
def check_numeric(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

#Checks that values entered by user are between 0 and 5
def check_bounds(value):
	if float(value) < 0 or float(value) > 5:
		return False
	else:
		return True

#Checks that user has filled all fields correctly
def check_valid():
	output.delete(1.0, "end-1c")
	if (not e1.get()
	or not e2.get()
	or not e3.get()
	or not e4.get()
	or not e5.get()):
		output.insert("end-1c", "All fields must be entered!")
		return False
	if (not check_numeric(e2.get())
	or not check_numeric(e3.get())
	or not check_numeric(e4.get())
	or not check_numeric(e5.get())):
		output.insert("end-1c", "Must be a positive numeric value!")
		return False
	if (not check_bounds(e2.get())
	or not check_bounds(e3.get())
	or not check_bounds(e4.get())
	or not check_bounds(e5.get())):
		output.insert("end-1c", "Number must be a positive value 5 or less!")
		return False
	else:
		return True

#Adds a new entry, or updates an entry with the same name
def	add_entry():
	global data
	if check_valid() == False:
		return
	new_startup = Startup(e1.get(),
							e2.get(),
							e3.get(),
							e4.get(),
							e5.get())
	if len(data) != 0:
		count = 0
		for x in data:
			if x.name == new_startup.name:
				data = data[:count]+[new_startup]+data[count + 1:]
				output.insert("end-1c", new_startup.name + " updated with a rating of " + new_startup.rating)
				return
			count += 1
	data.append(new_startup)
	output.insert("end-1c", new_startup.name + " added with a rating of " + new_startup.rating)

#Gives the total score of a start-up
def total_score(startup):
	return startup.fou_score + startup.ind_score + startup.tra_score + startup.gut_score

#Creates a list of all the scores
def	find_scores():
	ratings = []
	for x in data:
		ratings.append(total_score(x))
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

#Checks that the user has entered a positive number
def check_positive(value):
	if int(value) < 0:
		return False
	else:
		return True

#Prompts user to enter the number of businesses to invest in
def	business_number():
	output.delete(1.0, "end-1c")
	user_in = e6.get()
	if not user_in:
		output.insert("end-1c", "Please enter a number.")
		return
	if not check_numeric(user_in):
		output.insert("end-1c", "Must be a positive numeric value!")
		return
	if not check_positive(user_in):
		output.insert("end-1c", "Number must be a positive value!")
		return
	if not data:
		output.insert("end-1c", "No start-ups have been added.")
		return
	flag = False
	ratings = find_scores()
	count = 0
	while count < int(user_in):
		index = find_largest(ratings)
		if index >= 0:
			x = data[index]
			output.insert("end-1c", x.name + ", " + x.rating + "\n")
			flag = True
		elif flag == True and count < int(user_in):
			output.insert("end-1c", "No more start-ups meet the criteria.")
			return
		count += 1
	if flag == False:
		output.insert("end-1c", "There are no start-ups worth investing in :(")

#Shows all startups of the input type. If there are none, prints a seperate message
def present_all(comp):
	flag = False
	output.delete(1.0, "end-1c")
	for x in data:
		if x.rating == comp:
			if flag == False:
				output.insert("end-1c", comp + "s:\n")
			flag = True
			output.insert("end-1c", x.name + "\n")
	if flag == False:
		output.insert("end-1c", "No startup satisfied requirement for " + comp + " ratings.")

#Lists all of the startups
def	list_all():
	output.delete(1.0, "end-1c")
	flag = False
	for x in data:
		output.insert("end-1c", x.name + ", " + x.rating + "\n")
		flag = True
	if flag == False:
		output.insert("end-1c", "No start-ups have been added.")

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
	return str(round(average / total, 2))

#Find the number of startups meeting input criteria and appends all those startups to the list
def number_of(data, comp):
	count = 0
	for x in data:
		if x.rating == comp:
			count += 1
	return str(count)

#prints all result from task2
def	print_result():
	output.delete(1.0, "end-1c")
	if not data:
		output.insert("end-1c", "No start-ups have been added.")
		return
	total = len(data)
	output.insert("end-1c", "Number of Start-ups: " + str(total) + "\n")
	output.insert("end-1c", "Start-up progression rate: " + find_percent(data, total, "R") + "\n")
	output.insert("end-1c", "Average rating for factor 1: " + find_average(data, total, "founder") + "\n")
	output.insert("end-1c", "Average rating for factor 2: " + find_average(data, total, "industry") + "\n")
	output.insert("end-1c", "Average rating for factor 3: " + find_average(data, total, "traction") + "\n")
	output.insert("end-1c", "Average rating for factor 4: " + find_average(data, total, "gut") + "\n")
	output.insert("end-1c", "Number of P1s: " + number_of(data, "P1") + "\n")
	output.insert("end-1c", "Number of P2s: " + number_of(data, "P2") + "\n")
	output.insert("end-1c", "Number of P3s: " + number_of(data, "P3") + "\n")
	output.insert("end-1c", "Number of Rs: " + number_of(data, "R"))

#removes an element from the list given its name
def	remove_startup():
	output.delete(1.0, "end-1c")
	s_name = e1.get()
	if not s_name:
		output.insert("end-1c", "Please enter name of start-up to be removed.")
		return
	for x in data:
		if x.name == s_name:
			data.remove(x)
			output.insert("end-1c", s_name + " has been removed.")
			return
	output.insert("end-1c", "There is no start-up named " + s_name)


#Adds all start-ups from PDFs
data.append(Startup("FiveFour Inc", 3.5, 2, 4.75, 5))
data.append(Startup("Doggy Ties", 1, 1.5, 1, 0))
data.append(Startup("Letus Play", 4.5, 4, 4.5, 4))
data.append(Startup("Rural Distillery", 4.6, 5, 4.75, 4.5))
data.append(Startup("Acme Corp", 0.4, 1.2, 0.8, 0.2))
data.append(Startup("Litze", 3, 2.75, 2.1, 2))
data.append(Startup("Cakes for Days", 3.2, 2.8, 3.5, 3))
data.append(Startup("Abstrakt", 2, 2.5, 2.3, 2.6))
data.append(Startup("Performance Duds", 2.4, 2.25, 2.5, 2.5))
data.append(Startup("Baby Hatty", 2, 1.2, 1.1, 0.5))

#importing the graphical library
import tkinter as tk

#Creates a gui window
master = tk.Tk()
master.title("India Accelerator Start-up Evaluator")
#Create a number of labels with information on what to add
tk.Label(master, text="Start-up Name").grid(row=0, sticky=tk.W)
tk.Label(master, text="Founder Score").grid(row=1, sticky=tk.W)
tk.Label(master, text="Industry Score").grid(row=2, sticky=tk.W)
tk.Label(master, text="Traction Score").grid(row=3, sticky=tk.W)
tk.Label(master, text="Gut Score").grid(row=4, sticky=tk.W)

#Creates text-entry boxes for each of the above labels
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

#Places each of the text-entry boxes
e1.grid(row=0, column=1, sticky=tk.E)
e2.grid(row=1, column=1, sticky=tk.E)
e3.grid(row=2, column=1, sticky=tk.E)
e4.grid(row=3, column=1, sticky=tk.E)
e5.grid(row=4, column=1, sticky=tk.E)

#Buttons added for user to press for each option
tk.Button(master, text='Add/Update startup',
			command=add_entry).grid(row=5,
                            		column=1,
                                    sticky=tk.E,
                                    pady=4)
#Button to remove startup
tk.Button(master, text='Remove startup',
			command=remove_startup).grid(row=6,
                            		column=1,
                                    sticky=tk.E,
                                    pady=4)
tk.Button(master, text='Present all P1',
			command= lambda: present_all("P1")).grid(row=6,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Present all P2',
			command= lambda: present_all("P2")).grid(row=7,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Present all P3',
			command= lambda: present_all("P3")).grid(row=8,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Present all R',
			command= lambda: present_all("R")).grid(row=9,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
#Extra button for listing all start-ups
tk.Button(master, text='List all start-ups',
			command=list_all).grid(row=10,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Show general data',
			command=print_result).grid(row=11,
                            		column=0,
                                    sticky=tk.W,
                                    pady=4)
#new field, label and button for number of start-ups to invest in
e6 = tk.Entry(master)
tk.Label(master, text="How many start-ups would you like to invest in?").grid(row=12, columnspan=2, sticky=tk.W)
e6.grid(row=13, column=0)
tk.Button(master, text='Enter',
			command=business_number).grid(row=13,
                            		column=1,
                                    sticky=tk.W,
                                    pady=4)
#Sets the value of output to what is in the text box at the bottom. This is where everything is printed.
output = tk.Text(master, width = 50, height = 40)
output.grid(row=14, column=0, columnspan=2, sticky=tk.W, pady=4)
#Button to exit the program
tk.Button(master, text='Quit',
        	command=master.quit).grid(row=15,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
#Prevents the program from exiting until the user chooses to
tk.mainloop()
