"""
Given a string password, determine whether it is a valid password according to the specified rules.
Return "Strong" if the string is a valid password, "Weak" if it is not.
A valid password must follow these rules:
-- It must be at least 8 characters long.
-- It must contain at least one uppercase letter, one lowercase letter, and one numeral.
-- It must not contain any spaces.
Examples:
"Password123" is valid.
"password" is invalid.

Function Description
Complete the validatePassword function in the editor below.
validatePassword has the following parameter:
password (string): The password to be validated.
Prints
"Strong" if password is a valid password.
"Weak" if password is not a valid password.

"""

def validatePassword(password):
    if len(password) < 8:
        return "Weak"
    if " " in password:
        return "Weak"

    one_uppercase = any(i.isupper() for i in password)
    one_lowercase = any(i.islower() for i in password)
    one_digit = any(i.isdigit() for i in password)

    if one_uppercase and one_lowercase and one_digit:
        return "Strong"

    return "Weak"


if __name__ == '__main__':
    print(validatePassword("Password123"))
    print(validatePassword("password"))