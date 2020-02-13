# Age Calculator; calculates the age after asking a user for birth year

from datetime import date

today = date.today()
today = str(today)
current_year = int(today[0:4])

print(current_year)
birth_year = input("What year you were born: ") 
#birth_year = int(birth_year)
current_age = current_year - int(birth_year)

print('You are ' + str(current_age)+ ' years old!')