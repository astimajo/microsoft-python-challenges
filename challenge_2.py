yes = "yes" 
no = "no" 
yes1 = "y"
no1 = "n"

print("Would you like to continue?")
user_input = input()

if user_input == yes or user_input == yes1:
    print("Continuing ...")
    print("Complete!")

elif user_input == no1 or user_input == no1:
    print("Exiting")
else:
    print("Please try again with yes or no.")
