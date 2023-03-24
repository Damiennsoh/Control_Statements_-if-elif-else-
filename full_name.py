first_name = input("Enter first name here: ").strip() #Taking user input for first name
last_name = input("Enter last name here: ").strip() #Taking user inputs for last name
full_name = (first_name + " " + last_name)
if len(full_name) <= 0:
    print("You didn't enter anything")
else:
    print("My name is" + " " + full_name)





