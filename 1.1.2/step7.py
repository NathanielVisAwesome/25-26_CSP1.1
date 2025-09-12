import datetime as dt

# ask user for their name then welcome them
print("Welcome to the new year!")
user_name = input("What is your name?")
print("Hello,",user_name,"Welcome to the program!")

# ask user for their age
age = int(input("What is your age?"))

# get the current year using the datetime object that resides in the datetime module
curr_year = dt.datetime.now().year

# prepare and display output
birth_year = curr_year - age
print("Hmm... were you born in", birth_year, "?")