from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Fn to check users guess against actual answer
def  check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it..! The answer was {answer}.")

#Make a function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        # global turns
        # turns = EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else:
        # turns = HARD_LEVEL_TURNS
        return HARD_LEVEL_TURNS

def game():
#Choosing a random number from 1 to 100
    print("Welcome to the guessing game")
    print("I'm thinking of a number btw 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()
    # print(f"The number is {answer}")

#Repeat the guessing fn if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
#Let the user  guess a number
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of turns, you lose foo")
            return
        elif guess != answer:
            print("Guess again...")
#Track the number of turns and reduce by 1 if they get it wrong

game()