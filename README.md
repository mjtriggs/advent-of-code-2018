# advent-of-code-2018
https://adventofcode.com

This is my attempt at some of the code advent problems. I will try and do them all, but inevitably, I will get bored/stuck at some point and give up.

I'm also going to try and do this in Python to learn something, as I think with R it will either be too easy or too frustrating.

I also want to try and write unit tests for everything, just to try and encourage myself to follow best practices.

## What did I learn?

### Day 1
- Using `itertools` to cycle through the lists is far quicker than any loop
- Using a dictionary (i.e. curly brackets `{}`).

### Day 2
- Using `enumerate` to get an itemised list.
- Loading in a text file into a list
- Using `Counter` from `collections` to count the number of letters in a string.

### Day 3
- Regular Expressions (though I didn't really learn this - rather just copied all of this from Reddit)
- Using `defaultdict` to have a dictionary with a key and then multiple values.

### Day 4
- This is a really hard advent calendar! I think I prefer chocolate.
- Continued to use `defaultdict` from the previous day.
- Using the `.split()` function instead of regular expressions when all lines have a similar structure.
- `argmax()` to return the index/location of the maximum rather than a value.

### Day 5
- The solution on Reddit was so simple and clean for this, I just copied it and explained what was going on.
- Again we use list comprehension, but also the `.pop()` and `.append()` things are used. I'd particularly never seen `.pop()` before, but it could be useful.
- `ascii_lowercase` is imported from the `string` library as a reference string used in the second part.
