# This is for Day 4

# As a broad strategy, I think we need to list the events in time order, then
# get the minutes between 0000 and 0100 where each is sleeping, then somehow
# calculate the frequency of each minute per guard.

# Import libraries that we need
from collections import defaultdict
import numpy as np

# Load data
file = open('./day-4/data.txt', 'r')
data = file.read().split('\n')

# Sort data
data.sort()

# Function to parse the time from a string
def ParseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1] # Remove the square brackets
    return int(time.split(':')[1]) # Just return the minute

# Set up Dictionaries
guardDict = defaultdict(int)
guardTimeDict = defaultdict(int)

# Initialise guard/time parameters
guard = None
asleep = None

# Iterate through the sorted script
for line in data:
    if line:
        time = ParseTime(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:]) # Guard number as integer (drop #)
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                guardTimeDict[(guard, t)] += 1
                guardDict[(guard)] += 1

# Function to get the max values out of the Dictionaries
def argmax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

best_guard = argmax(guardDict)

timeVec = np.zeros(59)
for i in range(0, 59):
    timeVec[i] = guardTimeDict[(857, i)]
best_min = timeVec.argmax()

print(best_min * best_guard)

# For part 2
best_guard, best_min = argmax(guardTimeDict)
print(best_guard * best_min)
