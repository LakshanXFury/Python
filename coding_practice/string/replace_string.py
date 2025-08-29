def replace_string(input_data):
    new_text = input_data.replace(" ", "%20")
    print(f"The replaced string is: {new_text}")


user_input = input(str("Enter a String with Space: "))
replace_string(user_input)

