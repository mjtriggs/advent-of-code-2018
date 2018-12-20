# Day 1

# We need to write something to read in a list of numbers (with +/- before) and
# from a given starting value, produce a final output.

from loadData import numList
from itertools import cycle

def GetResultingFrequency(startingVal, list):
    return startingVal + sum(list)

print(GetResultingFrequency(0, numList))

def FreqReachedTwice(startingVal, input):
    freq = startingVal
    seen = {startingVal}
    for num in cycle(input):
        freq += num
        if freq in seen:
            return freq
            break
        seen.add(freq)

print(FreqReachedTwice(0, numList))
