"""
Write code to Check if two strings are Anagram or not
"""

def anagram(string1: str, string2: str):
    # Convert to lowercase
    str1 = string1.lower()
    str2 = string2.lower()

    # Remove spaces and punctuation
    cleaned_str1 = ""
    cleaned_str2 = ""

    for ch in str1:
        if ch.isalnum():   # keeps only letters and numbers
            cleaned_str1 += ch

    for ch in str2:
        if ch.isalnum():
            cleaned_str2 += ch

    # Compare sorted characters
    if sorted(cleaned_str1) == sorted(cleaned_str2):
        print("It is an Anagram")
    else:
        print("It is not an Anagram")


anagram("listen", "silent")
anagram("rail safety", "fairy tales")
anagram("Dormitory!", "Dirty room")
anagram("hello", "world")
