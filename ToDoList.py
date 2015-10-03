#NOTE: Final project

Rena_to_do = {"Shopping":"Groceries", "Pay_Bills":"Rent", "Pay_Utilities":"Water, Heat and Electric", "Repair": "Car", "Pet_Care": "Dog grooming"}

print "Welcome to Rena's TO DO List!"
while(True):
	instructions = "Type A to see list., Type B to see Shopping, Type C to see Pay_Bills, Type D to see Pay_Utilities, Type E to see Repair, Type F to see Pet_Care, Type X for Exit. "
	user_answer = raw_input(instructions) #NOTE: Takes the input from user and stores it in the variable labeled user_answer.
	if user_answer.upper() == "A": #Note: "A" is the expected answer that the user will type. You are also checking to see if user is typing "A", otherwise it won't print list.
		print Rena_to_do
	elif user_answer.upper() == "B":
		print Rena_to_do['Shopping']
	elif user_answer.upper() == "C":
		print Rena_to_do['Pay_Bills']
	elif user_answer.upper() == "D":
		print Rena_to_do['Pay_Utilities']
	elif user_answer.upper() == "E":
		print Rena_to_do['Repair']
	elif user_answer.upper() == "F":
		print Rena_to_do['Pet_Care']
	elif user_answer.upper() == "X":
		print "Exiting the List. Good-bye!"
		break
	else:
		print "Ooops! Please try again!"
	print "********************************************"


# complete_tasks = {}
# for x in complete_tasks:
# 	print x
# 	if x in complete_tasks:
# 		complete_tasks[x] = complete_tasks[x] + 1
# 	else:
# 		complete_tasks[x] = 1
# print complete_tasks

	


