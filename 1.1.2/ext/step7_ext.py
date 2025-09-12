import datetime as dt
from turtledemo.clock import current_day

# ask user for their name then welcome them
print("Welcome to the new year!")
user_name = input("What is your name?")
print("Hello,",user_name,"You are not supposed to be here.")

# ask user for their age
month = int(input("What month were you born?"))
day = int(input("What day were you born?"))
year = int(input("What year were you born?"))

# get the current year using the datetime object that resides in the datetime module
curr_year = dt.datetime.now().year
curr_day = dt.datetime.now().day
curr_month = dt.datetime.now().month

# prepare and display output
birth_month = curr_month - month
birth_day = curr_day - day
birth_year = curr_year - year
print("Hmm... were you born on",birth_month, birth_day, birth_year, "?")