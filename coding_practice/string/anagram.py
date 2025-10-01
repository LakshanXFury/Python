# Check if two strings are anagrams.
"""
A word or phrase that is made by arranging the letters of another word or phrase in a different order.
Fried = Fired, Listen = Silent
"""


def anagram(first_word, second_word):
    a = first_word.replace(" ", "").lower()
    b = second_word.replace(" ", "").lower()

    lista = sorted(list(a))
    listb = sorted(list(b))

    if lista == listb:
        print("Your words are Anagram")
    else:
        print("Your words are not an Anagram")


anagram("the eyes", "They see")
anagram("study", "dusty")
