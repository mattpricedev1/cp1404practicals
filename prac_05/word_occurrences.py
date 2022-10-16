"""
Word Occurrences
Estimate: 60 minutes
Actual:
"""

word_to_count = {}
user_string = input("Enter a string: ")
words = user_string.split()

for word in words:
    try:
        count = word_to_count.get(word, 0)
        word_to_count[word] = count + 1
    except KeyError:
        print("Error")
print(word_to_count)