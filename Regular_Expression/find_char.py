import re

full_string = "robotFrame@Work#python@125"

string = len(re.findall(r"[a-zA-Z]", full_string))
number = len(re.findall(r"\d", full_string))
character = len(re.findall(r"[^a-zA-Z0-9]", full_string))

print(string)
print(number)
print(character)