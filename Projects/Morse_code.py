# Text to Morse code

text = input("Enter the text that you want to convert into Morse code: ")

split_version = [*text]  #Un-packing operator

# print(split_version)

dictionary = {
  "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
  "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
  "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."
}


for letter in split_version:
    upper_case = letter.upper()
    # print(upper_case)
    if upper_case in dictionary:  # Check if the letter exists in the dictionary
        print(dictionary[upper_case], ",", end="")
    else:
        print(f"Enter words only from A-Z as this is {upper_case} not a letter")

