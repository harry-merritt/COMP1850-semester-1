# Worksheet 1.2: Task 2 Solution

import util, sys

numbers = util.read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")



minimum = min(numbers)
maximum = max(numbers)
length = len(numbers)
meanavg = sum(numbers) / length

if length % 2 == 0:
    # Even case
    median = numbers[length / 2] + numbers[(length / 2) + 1]
    median = median / 2
else:
    # Odd case
    median = numbers[(length + 1) / 2]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {meanavg}")
print(f"Median = {median}")