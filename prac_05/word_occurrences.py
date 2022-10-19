"""
Word Occurrences
Estimate: 60 minutes
Actual: 90 minutes
"""

word_to_count = {}  # initialise empty dictionary
user_string = input("Enter a string: ")
words = user_string.split()  # convert string to list

for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1  # add word and occurrence to dictionary

# display words that occur more than once only once in the list
words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} occurred {word_to_count[word]} time(s)")
