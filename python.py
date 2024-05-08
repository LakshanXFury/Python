import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
wordlength = len(chosen_word)
for _ in range(wordlength):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()
for position in range(wordlength):
  letter = chosen_word[position]
  if letter == guess:
      display[position]=letter
print(display)
