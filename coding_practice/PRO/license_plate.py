"""
Return "Standard" if the string is a valid standard license plate number, "Special" if it is a valid special license
plate number, or "Neither" i it is not a valid license plate number of any type. if A valid standard license
plate number is in the form "ABC-1234" where: ABC is a sequence of 3 uppercase letters. 1234 is a sequence of 4 digits.

Examples: "XYZ-1234" is valid. "XY-12345" is invalid. A valid special license plate number is in the form "AB-12345"
where: AB is a sequence of 2 uppercase letters. 12345 is a sequence of 5 digits. Examples: "AB-12345" is valid.
"A-123456" is invalid.
"""
import re

def validatePlate(queryPlate):
    if re.fullmatch(r"[A-Z]{3}-\d{4}", queryPlate):
        return "Standard"
    if re.fullmatch(r"[A-Z]{2}-\d{5}", queryPlate):
        return "Special"
    return "Neither"


def licensePlate(queryPlate):
    splitplate = queryPlate.split("-")

    if len(splitplate) != 2:
        return "Neither"

    first, second = splitplate

    if first.isupper() and first.isalpha():
        if len(first) == 3 and len(second) == 4 and second.isdigit():
            return "Standard"
        if len(first) == 2 and len(second) == 5 and second.isdigit():
            return "Special"
            
    return "Neither"



query = input("Enter the license plate: ").strip()
result = validatePlate(query)
print(result)

print(licensePlate(query))

"""
XYZ-1234
ABC-12345
A-1234
"""