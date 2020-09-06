while True:
    word = input("Give me a word:")
    word.replace(" ","")
    reversed_word = word[::-1]
    if word == reversed_word:
        print("It's a palindrome!")
    else: 
        print("It's not a palindrome!")