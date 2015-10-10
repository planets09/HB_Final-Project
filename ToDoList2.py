#NOTE: Final project

Rena_to_do = {"Shopping":"Groceries", "Pay_Bills":"Rent", "Pay_Utilities":"Water, Heat and Electric", "Repair": "Car", "Pet_Care": "Dog grooming"}

print "Welcome to Rena's TO DO List!"

while(True):
	instructions = "Type list to see whole list. Next, type in the name of TO DO you would like to finish. Or, if you want to add to the list, type modify."
	instructions2 = "Type in item name."
	instructions3 = "Provide description of item."
	user_answer = raw_input(instructions) #NOTE: Takes the input from user and stores it in the variable labeled user_answer.
	if user_answer.lower() == "list": #Note: "A" is the expected answer that the user will type. You are also checking to see if user is typing "A", otherwise it won't print list.
		print Rena_to_do
	elif user_answer.lower() == "modify":
		user_answer2 = raw_input(instructions2)
		user_answer3 = raw_input(instructions3)
		Rena_to_do[user_answer2] = user_answer3
		print Rena_to_do
	elif user_answer.lower() == "shopping":
		del Rena_to_do['Shopping']
	elif user_answer.lower() == "pay_bills":
		del Rena_to_do['Pay_Bills']
	elif user_answer.lower() == "pay_utilities":
		del Rena_to_do['Pay_Utilities']
	elif user_answer.lower() == "repair":
		del Rena_to_do['Repair']
	elif user_answer.lower() == "pet_care":
		del Rena_to_do['Pet_Care']
	elif user_answer.lower() == 'x':
		print "Exiting the List. Good-bye!"
		break
	else:
		print "Ooops! Please try again!"
	print "********************************************"



	


