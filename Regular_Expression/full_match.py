import re

# Use (com|in|org) with | as OR to whitelist only specific extensions you want to allow.
pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|in|org)"

input_data = input(str("Enter the email address: "))

if re.fullmatch(pattern, input_data):
    print("Success")
else:
    print("Failure")