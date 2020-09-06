import random

# Returns the user's input
def get_integer(message = "Enter a number: ", reqLength = 0):
    # Uses try to check in pInput is an integer when converting
    try:
        # Gets the input
        pInput = input(message)
        # Checks if reqLength was set
        if len(pInput) == 0:
            pass
        # Checks if the user's input matches reqLength
        elif len(pInput) != reqLength:
            # If not, asks for input again
            print(f"Invalid length. (Required Length: {reqLength})")
            get_integer(message, reqLength)
        else:
            # If it matches, will return pInput as integer
            return int(pInput)
    except:
        # Runs if pInput is not an integer
        print("Encountered an error.")
        get_integer(message, reqLength)

# Returns a list of the characters in the string given
def split(string):
        return [char for char in string]  

while True:
    # Gets random number
    answer = random.randint(1111,9999)
    # Calls split() function for checking later on
    splitAnswer = split(str(answer))
    playing = 0
    # Loops until the user gives "Y" as an input
    while playing != "Y":
        playing = str(input("Start playing? (Y) \n"))
    while playing == "Y":
        # Calls get_integer() function to get the player's guess.
        guess = get_integer("Enter your guess: ", 4)
        # Splits the guess into a list of characters.
        splitGuess = split(str(guess))
        # Creates list of values that are in splitAnswer and splitGuess
        cows = [i for i in splitGuess if i in splitAnswer]
        # The amount of cows therefore is the length of the list
        cows = len(cows)
        bulls = 0
        # Just checks each index of splitGuess and splitAnswer to see if they are the same
        for i in range(4):
            if splitGuess[i] == splitAnswer[i]:
                bulls += 1
        # Prints out their score
        print(f"You've got {cows} cows and {bulls} bulls.")
        if int(answer) == int(guess):
            print("Correct!")
            break