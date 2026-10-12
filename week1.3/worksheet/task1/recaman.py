# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]

while len(sequence) != L:

    next = sequence[-1] - len(sequence) # length is k of last item + 1
    if next <= 0 or next in sequence:
        next = sequence[-1] + len(sequence)

    sequence.append(next)

print(*sequence) # God I love the splat operator