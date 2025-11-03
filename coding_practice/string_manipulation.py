"""
Write a function to count how many times each word appears in a sentence, ignoring case and punctuation
"""


def string_manipulation(string_value):
    lowercase_the_string = string_value.lower()

    # Remove punctuation
    punctuation = ".,!?;:'\"-()"  # list of punctuation marks
    clean_sentence = ""

    for char in lowercase_the_string:
        if char not in punctuation:
            clean_sentence += char

    print(f"After removing the punctuation from the string :{clean_sentence}")

    # Using split method to split into words
    split_into_words = clean_sentence.split()
    print(f"Converting the string into words :{split_into_words}")

    # To convert the words into a single string we can use join method

    d = {}
    for each_words in split_into_words:
        if each_words in d:
            d[each_words] += 1
        else:
            d[each_words] = 1

    print(f"The is how many time a word has repeated :\n {d}")


string_manipulation("hello ? hello , how are you")



# To remove punctuation using Regular expression
# Using re (regular expressions, more powerful)
# import re
#
# def remove_punctuation(sentence):
#     return re.sub(r'[^\w\s]', '', sentence)
#
#
# Explanation:
#
# \w → means “letters, digits, and underscores”
#
# \s → means “spaces”
#
# [^...] → means “everything except these”
#
# So this removes anything that’s not a letter, number, or space.