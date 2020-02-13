# Age Calculator; calculates the age after asking a user for birth year

#import date form datetime library 
from datetime import date

#store today's date in variable 'today'
today = date.today()

#convert it to string type from date
today = str(today)

# slice off the extra chars to find out the current year
current_year = int(today[0:4])

# get user's input in YYYY format
birth_year = input("What year you were born: ") 

# calculate current_age by subracting birth_year from current_year
current_age = current_year - int(birth_year)

#print age
print('You are ' + str(current_age)+ ' years old!')