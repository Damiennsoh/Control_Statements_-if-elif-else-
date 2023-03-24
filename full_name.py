#This program uses if, elif and the else statements to execute a block of codes under them based on certain conditions
# In control decisions like this, it's worht noting that the if statement comes first, followed by one or more elif statements and a single else statement to bring the flow of the program to an end.

first_name = input("Enter first name here: ").replace(" ", "") # By adding the replace method, it replaces all occurrences of whitespace characters (including spaces, tabs, and newlines) with an empty string "" this ensures that any trailing whitespace is removed from input strings before the concatenation of the first_name and last_name to form the full_name.
last_name = input("Enter last name here: ").replace(" ", "") # This also replaces any trailing whitespace.
full_name = (first_name + " " + last_name)
if len(full_name) <= 0: #If the user does not make any input, the code under the if statement executes.     
    print("You didn't enter anything. Please enter your full name.")
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your first name and last name")
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure you have only entered your full name")
else:
    print("Thank you for entering your full name") # The else statement brings the code execution to an end.





