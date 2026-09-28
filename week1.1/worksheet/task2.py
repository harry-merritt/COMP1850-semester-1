"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

monthly = input("How much would you like to save each month? ")
try:
    monthly = int(monthly)
except:
    print("Invalid amount.")
    quit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly = monthly * 12
print(f"In a year, you will save £{yearly}.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = yearly * 1.008 # need to add zeroes to the end only if needed
rounded = round(interest, 2)
print(f"With interest, you will save £{rounded:.2f}") # Learned something new, didn't know modifers were a thing