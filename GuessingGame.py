import random
guesses = 0
while True:
    guess = 0
    answer = random.randint(1,100)
    print(answer)
    guessNo = 0
    while guess != answer:
        guessNo += 1     
        guess = input("Your guess:")
        if guess.lower() == "exit":
            exit = 1
            break
        if not guess.isdecimal():
            print("Not a valid guess!")
            continue
        guess = int(guess)
        if guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
        elif guess == answer:
            print(f"Correct! You got it on guess #{guessNo}")
    guesses += 1
    if exit == 1:
        break
print(f"Game over! You got {guesses} guesses correct!")