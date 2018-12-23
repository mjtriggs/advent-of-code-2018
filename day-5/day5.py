# Day 5 - Polymers
# I didn't do this - taken from Reddit

# Load packages and functions
from string import *

# Load Data
s = open('day-5/data.txt').read().strip()

# Define function
def collapse(s):
    p = ['.'] # p is the comparison string that hasn't been removed
    for u in s:
        v = p[-1] # Take the most recent entry of p
        if v != u and v.lower() == u.lower():
            # If the most recent entry and the new one react,
            # then remove the most recent entry
            p.pop()
        else:
            # If there is no reaction, add the latest value to p
            p.append(u)
    return len(p) - 1

print(collapse(s))

print(min(collapse(c for c in s if c.lower() != x) for x in ascii_lowercase))

# Explanation:
# This is another example of list comprehension
# `for x in ascii_lowercase` just makes sure we look at letters in the string
# `c for c in s` looks at individual characters in the string
# `c.lower != x` keeps remaining items with that polymer removed
# The min just takes the smallest output out of the repeated collapse functions
