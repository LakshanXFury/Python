PLACEHOLDER = "[Friend's Name]"


with open("C:/Users/lakshas/Desktop/python/MailMerging/Input/Names/Invited_name.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("C:/Users/lakshas/Desktop/python/MailMerging/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"C:/Users/lakshas/Desktop/python/MailMerging/Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)