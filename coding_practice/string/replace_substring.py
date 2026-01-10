"""
Write a code to replace a substring in a string.

"""

def replace_substring(str1, str2, str3):
    final_string = str1.replace(str2, str3)
    print(f"The string after replacing: {final_string}")



original = input("Enter a string: ")
to_replace = input("Enter the substring you want to replace : ")
replacement = input("Enter the string you want to replace with: ")

replace_substring(original,to_replace,replacement)



