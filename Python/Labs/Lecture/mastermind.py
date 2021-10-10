import random

def get_guess():
    return list(input("What is your guess? "))

def generate_code():
    digits = [str(num) for num in range(10)]
    print(digits, '<------')
    random.shuffle(digits)
    print(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    # Takes in a user guess and code then compares the numbers in a loop and
    # creates a list of clues according to the matching parameters.

    if userGuess == code:
        return "CODE CRACKED"
    clues = []
    # Compare guess to code
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
secretCode = generate_code()
print(secretCode)
print("Code has been generated, please guess a 3 digit number")

clueReport = []
while clueReport != "CODE CRACKED":
    # Ask for guess
    guess = get_guess()
    # Give the clues
    clueReport = generate_clues(guess,secretCode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
