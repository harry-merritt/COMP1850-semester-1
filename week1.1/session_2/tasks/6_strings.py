# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # all to lowercase
print(f"Modified String 2: {user_string.upper()}") # all to uppercase
print(f"Modified String 3: {user_string.strip()}") # removes whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces a with @
print(f"Modified String 5: {user_string.capitalize()}") # makes first letter only capitalised
print(f"Modified String 6: {user_string[::-1]}") # reverses string
print(f"Modified String 7: {user_string.title()}") # tilecases the string
print(f"Modified String 8: {len(user_string)}") # returns the length of the string
print(f"Modified String 9: {user_string.find('a')}") # returns the position of a
print(f"Modified String 10: {user_string.count('a')}") # returns the number of as
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks if it starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}") # checks if it starts with !
print(f"Modified String 13: {user_string.isalnum()}") # checks if it is alphanumeric
print(f"Modified String 14: {user_string.isalpha()}") # checks if it alphabetic
print(f"Modified String 15: {user_string.isdigit()}") # checks if it is a number



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!