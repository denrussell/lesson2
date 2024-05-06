# Objective:
# Dive deep into the intricacies of the calendar by exploring the concept of leap years.

# Task 1: Leap Year Checker
# Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not 
# and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

# Expected Outcome: If you test the year 1900, is should be False. The year 2000 should be True. The year 2024 should be True

# Ask the user to input a year. Make it an integer.
year = int(input("Please enter year: "))
                       
# Assign variable for the year divisible by 4 with 0 remainder.
# Assign variable for the year divisible by 100 with 0 remainder.
# Assign variable for the year divisible by 400 with 0 remainder.
leap = year % 4 == 0
notleap = year % 100 == 0
leap400 = year % 100 == 0 and year % 400 == 0



if leap400:
    print("Answer: ",year,"is a leap year.")   
elif notleap:
    print("Answer: ",year,"is NOT a leap year.")
elif leap:
    print("Answer: ",year,"is a leap year.")
else:
    print("Answer: ",year,"is NOT a leap year.")



# There's a lot of trial and error that I did here.
# In the end it was a matter of which should come first.
# Also had to play with and operator

