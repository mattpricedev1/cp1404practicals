"""
Word Occurrences
Estimate: 60 minutes
Actual:
"""

word_to_count = {}  # empty dictionary
user_string = input("Enter a string: ")
words = user_string.split()  # convert string to list

for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1
    print(f"{word} : {word_to_count[word]}")
