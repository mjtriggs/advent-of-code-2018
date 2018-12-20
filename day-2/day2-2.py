# Day 2 - Part 2

from itertools import combinations

# Load in Text File
file = open('./day-2/data.txt', 'r')
data = file.readlines()

for i in data:
    for j in data:
        diffs = 0
        for idx, val in enumerate(i):
            if val != j[idx]:
                diffs += 1
        if diffs == 1:
            ans = [val for idx, val in enumerate(i) if j[idx] == val]
            print(''.join(ans))

# Most of this solution came from Reddit
