# Day 2 relates to counting the number of different letters in a string.
# From what I understand, if a string contains exactly two of the same letter it
# counts for a '2', and if it contains exactly three of the same letter, it
# counts for a '3'. For the list of strings that we submit, we want to do the
# product of 2s and 3s.

# As a general approach, let's count the number of times letters occur in a
# string, then work from this point onwards.

from collections import Counter

def CountLetters(string):
    d = Counter(string)
    return(d)

def IsCount(d, num):
    list = []
    for key, value in d.items():
        if value == num:
            list.append(key)
    if len(list) >= 1:
        return(True)
    else:
        return(False)

def CalculateChecksum(ls):
    num_2 = len([x for x in data if IsCount(CountLetters(x), 2) == True])
    num_3 = len([x for x in data if IsCount(CountLetters(x), 3) == True])
    return(num_2 * num_3)

# Load in Text File
file = open('./day-2/data.txt', 'r')
data = file.readlines()

print(CalculateChecksum(data))
