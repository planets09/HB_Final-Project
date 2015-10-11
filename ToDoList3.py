#NOTE: Final project

Rena_to_do = {"shopping":"groceries", "pay_bills":"rent", "pay_utilities":"water, heat and electric", "repair": "car", "pet_care": "dog grooming"}

print "Welcome to Rena's TO DO List!"

while(True):
	instructions = "Type list to see whole list. Next, type in delete if item has been completed. Or, if you want to add to the list, type add. Type exit to exit list."
	instructions2 = "Type in item name."
	instructions3 = "Provide description of item."
	instructions4 = "Please type in name of item that has been completed."
	user_answer = raw_input(instructions) #NOTE: Takes the input from user and stores it in the variable labeled user_answer.
	if user_answer.lower() == "list": #Note: "list" is the expected answer that the user will type. You are also checking to see if user is typing "list", otherwise it won't print list.
		for item in Rena_to_do:
			print item, Rena_to_do[item]
	elif user_answer.lower() == "add":
		user_answer2 = raw_input(instructions2)
		user_answer3 = raw_input(instructions3)
		Rena_to_do[user_answer2.lower()] = user_answer3.lower()
		for item in Rena_to_do:
			print item, Rena_to_do[item]
	elif user_answer.lower() == "delete":
		user_answer4 = raw_input(instructions4).lower()
		if user_answer4 in Rena_to_do:
			del Rena_to_do[user_answer4]
			for item in Rena_to_do:
				print item, Rena_to_do[item]
		else:
			print "Sorry, item not found!"
	elif user_answer.lower() == 'exit':
		print "Exiting the List. Good-bye!"
		break
	else:
		print "Ooops! Please try again!"
	print "********************************************"



	


