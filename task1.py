def	rating(founder, industry, traction, guts):
	score = float(founder) * .3 + float(industry) * .3 + float(traction) *.35 + float(guts) * .05
	if score >= 4:
			print("P1")
	elif score >= 2.5:
			print("P2")
	elif score >= 1:
			print("P3")
	else:
			print("R")

user_in = input("Enter a Start-up’s factor ratings (separated by comma):")
input_split = user_in.split(",")
rating(input_split[1], input_split[2], input_split[3], input_split[4])