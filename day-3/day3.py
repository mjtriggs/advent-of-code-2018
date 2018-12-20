# This is quite complicated and I've had to copy a large part of this from
# the subreddit.

from collections import defaultdict
import re

# Load in Text File
file = open('./day-3/data.txt', 'r')
data = file.readlines()

# Regular Expressions copied from Reddit here:
# https://www.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/eazev7m
# Further explanation: https://www.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/eb04qj5
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

# I think that this sets up a dictionary with a counts. I imagine that the
# approach here is to create a dictionary entry for every square, and then label
# each dictionary entry with the claim ID
m = defaultdict(list)
overlaps = {}

# Now we do the list comprehension on the mapped values
for (claim_number, start_x, start_y, width, height) in claims:
    # Don't know what this next line does
    overlaps[claim_number] = set()
    # For each list of claims, we go through every available space
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            if m[(i,j)]:
                # If the space already exists in the dictionary, then add the
                # the claim number onto the other fields
                for number in m[(i, j)]:
                    overlaps[number].add(claim_number) # Add both ways
                    overlaps[claim_number].add(number) # Add both ways
            m[(i,j)].append(claim_number) # Add this to the dictionary object

print(len([k for k in m if len(m[k]) > 1]))

print([k for k in overlaps if len(overlaps[k]) == 0][0])
