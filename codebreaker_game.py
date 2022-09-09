
# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match, the game will report "CODE CRACKED"!

import random

# welcome the player
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")


# Create a Secret Code - a list of 3 digit, non repeating
def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return digits[:3]


secret_code = generate_code()

# tell the player that a code has been generated
print("Code has been generated, please guess a 3 digit number")


# generating clues for the user
def generate_clues(code, user_guess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and
    creates a list of clues according to the matching parameters.
    '''
    if user_guess == code:
        return "CODE CRACKED"

    clues = []

    # Compare guess to code
    for index, num in enumerate(user_guess):
        if num == code[index]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues


# Empty Clue Report to Start with
clueReport = []

# Keep asking until the user has gotten it right!
while clueReport != "CODE CRACKED":

    # Ask for guess
    guess = list(input("What is your guess?"))

    # Give the clues
    clueReport = generate_clues(guess, secret_code)

    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
