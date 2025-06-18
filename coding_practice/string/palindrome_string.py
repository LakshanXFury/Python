# Check if a string is a palindrome.

def is_palindrome(string):
    string = string.replace(" ", "").lower()  # Remove spaces
    return string == string[::-1]


print(is_palindrome("malayalam"))
print(is_palindrome("lakshan"))