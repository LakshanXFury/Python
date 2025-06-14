def vowels_in_string(string_value):
    vowels = set("aeiouAEIOU") # Set is used to make it faster

    vowel_count = 0

    for char in string_value:

        if char in vowels:
            vowel_count += 1

    return vowel_count


string_input = str(input("Enter the string that you want to check the vowels for: "))

# You wanted to call the function with the user's input and print the result
# To do that, you need to invoke the function by adding parentheses and passing the argument:

print(f"The vowel count in the entered string is: {vowels_in_string(string_input)}")
